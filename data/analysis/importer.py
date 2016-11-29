import re

from datetime import datetime
from dateutil.relativedelta import relativedelta

import engine
import data.search.elastic as elastic

from models.exceptions import DataIntegrityError
from models.employer import Employer
from models.job import Job
from models.applicant import Applicant
from models.location import Location
from models.comment import Comment
from models.job_keyword import Keyword
from models.rating import AggregateRating
import models.term as Term
import models.program as Program
import models.employer_alias as employer_alias

import shared.logger as logger


COMPONENT = 'Importer'


def import_job(**kwargs):
    """Import job from Jobmine.

    Keyword arguments:
    employer_name -- Employer name
    job_title -- Title of job
    summary -- Job summary
    year -- Year the job was advertised
    term -- Term job was advertised [Fall, Winter, Spring]
    location -- Location job was advertised
    openings -- Number of job openings
    remaining -- Number of job openings remaining
    applicants -- Number of applicants job has (Optional)
    levels -- Levels job is intended for [Junior, Intermediate, Senior]
    programs -- Programs the job is specified for
    url -- URL of job in Jobmine
    date -- Date job was crawled (useful for knowing exactly # of applicants at what time)
    index -- Boolean to indicate whether to index or not (default True)
    """

    employer_name = kwargs['employer_name'].lower()

    job_title = kwargs['job_title'].lower()

    term = kwargs['term']

    levels = []

    for level in kwargs['levels']:
        uw_level = Term.get_level(level)
        if uw_level:
            levels.append(uw_level)
        else:
            logger.error(COMPONENT, 'Error processing level: {}'.format(level))

    programs = []

    for program in kwargs['programs']:
        uw_program = Program.get_program(program)
        if uw_program:
            programs.append(uw_program)
        else:
            logger.error(COMPONENT, 'Error processing program: {}'.format(program))

    location = kwargs['location'].lower()

    openings = int(kwargs['openings'])

    remaining = int(kwargs['remaining']) if 'remaining' in kwargs else openings

    summary = kwargs['summary']

    filtered_summary = engine.filter_summary(summary)

    summary_keywords = engine.get_keywords(filtered_summary, programs)

    date = kwargs['date']

    year = date.year

    url = kwargs['url']

    applicants = 0

    try:
        if kwargs['applicants']:
            applicants = int(kwargs['applicants'])
    except Exception:
        pass

    index = True

    if index in kwargs:
        index = kwargs['index']

    logger.info(COMPONENT, 'Importing job: {} from {}'.format(job_title, employer_name))

    # If employer does not exist, create it
    if not Employer.employer_exists(employer_name):
        logger.info(COMPONENT, 'Employer: {} does not exist, creating..'.format(employer_name))

        employer = Employer(name=employer_name)

        logger.info(COMPONENT, 'Creating job: {}'.format(job_title))

        location = Location(name=location)

        applicant = Applicant(applicants=applicants, date=date)

        keywords = [Keyword(keyword=k['keyword'], types=k['types']) for k in summary_keywords]

        # New job so number of remaining positions is same as openings
        job = Job(title=job_title, summary=filtered_summary, year=year,
                  term=term, location=[location], openings=openings, remaining=remaining,
                  applicants=[applicant], levels=levels, programs=programs, url=url,
                  keywords=keywords)

        job.save()
        job.reload()

        employer.jobs.append(job)
        employer.save()
        employer.reload()

        if index:
            elastic.index_employer_jobmine(employer)
            elastic.index_job_jobmine(employer, job)

    # Employer already exists
    else:
        employer = Employer.objects(name=employer_name).no_dereference().first()

        logger.info(COMPONENT, 'Employer: {} already exists'.format(employer_name))

        # If job does not exist, create it
        if not employer.job_exists(job_title):
            logger.info(COMPONENT, 'Creating job: {}'.format(job_title))

            location = Location(name=location)

            applicant = Applicant(applicants=applicants, date=date)

            keywords = [Keyword(keyword=k['keyword'], types=k['types']) for k in summary_keywords]

            # New job so number of remaining positions is same as openings
            job = Job(title=job_title, summary=engine.filter_summary(summary), year=year,
                      term=term, location=[location], openings=openings, remaining=remaining,
                      applicants=[applicant], levels=levels, programs=programs, url=url,
                      keywords=keywords)

            job.save()
            job.reload()

            employer.update(push__jobs=job)

            if index:
                elastic.update_employer_jobmine(employer)
                elastic.index_job_jobmine(employer, job)

        # Job already exists
        else:
            logger.info(COMPONENT, 'Job: {} already exists'.format(job_title))

            job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

            if not year >= job.year:
                raise DataIntegrityError('Job: {} by {} cannot be advertised before {}'
                                         .format(job_title, employer_name, job.year))

            filtered_summary_compare = re.sub(r'\W+', '', filtered_summary.lower().strip()).strip()
            job_summary_compare = re.sub(r'\W+', '', job.summary.lower().strip()).strip()

            # Job summary is not the same. In this case the employer most likely changed the job
            if not filtered_summary_compare == job_summary_compare:

                if openings >= 1:
                    logger.info(COMPONENT, 'Job: {}: different summary detected, deprecating and creating new job..'
                                .format(job_title))

                    job.update(set__deprecated=True)

                    location = Location(name=location)

                    applicant = Applicant(applicants=applicants, date=date)

                    keywords = [Keyword(keyword=k['keyword'], types=k['types']) for k in summary_keywords]

                    # Assume new job so number of remaining positions is same as openings
                    new_job = Job(title=job_title, summary=filtered_summary, year=year, term=term,
                                  location=[location], openings=openings, remaining=remaining, applicants=[applicant],
                                  levels=levels, programs=programs, url=url, keywords=keywords)

                    new_job.save()
                    new_job.reload()

                    employer.update(push__jobs=new_job)

                    if index:
                        elastic.delete_employer_jobmine(employer)
                        elastic.delete_job_jobmine(employer, job)
                        elastic.index_employer_jobmine(employer)
                        elastic.index_job_jobmine(employer, new_job)
                else:
                    logger.info(COMPONENT, 'Job: {}: different summary detected but invalid openings: {}, ignoring..'
                                .format(job_title, openings))

            # Job is the same (same title and description)
            else:
                # If job is being advertised in new term
                if year != job.year or term != job.term:
                    logger.info(COMPONENT, 'Job: {}: being advertised in new term, updating..'.format(job_title))

                    # Add hire ratio for previous term
                    hire_ratio = float(job.openings - job.remaining) / job.openings
                    
                    job.hire_rate.add_rating(hire_ratio)

                    location = Location(name=location)

                    applicant = Applicant(applicants=applicants, date=date)

                    hire_rate = AggregateRating(rating=job.hire_rate.rating, count=job.hire_rate.count)
                    
                    job.update(set__year=year, set__term=term, add_to_set__location=location, set__openings=openings,
                               set__remaining=remaining, push__applicants=applicant, set__hire_rate=hire_rate,
                               set__levels=levels, set__programs=programs, set__url=url, set__last_indexed=datetime.now())

                    if index:
                        elastic.update_job_jobmine(employer, job)

                # Job is being updated. We need to update location, openings, levels, remaining, hire_rate, applicants
                else:
                    logger.info(COMPONENT, 'Job: {}: updating for current term'.format(job_title))

                    remaining = job.remaining

                    # Job posting has decreased, some positions filled up
                    if openings < remaining:
                        remaining = openings

                    location = Location(name=location)

                    applicant = Applicant(applicants=applicants, date=date)

                    job.update(add_to_set__location=location, set__remaining=remaining,
                               set__levels=list(set(levels + job.levels)), push__applicants=applicant,
                               set__programs=list(set(programs + job.programs)), set__url=url,
                               set__last_indexed=datetime.now())

                    if index:
                        elastic.update_job_jobmine(employer, job)


def update_job(**kwargs):
    """Update job from Jobmine.

    Keyword arguments:
    id -- Job ID
    summary -- Job summary
    location -- Location job was advertised
    programs -- Programs the job is specified for
    levels -- Levels job is intended for [Junior, Intermediate, Senior]
    openings -- Number of job openings
    index -- Boolean to indicate whether to index or not (default True)
    """

    summary = kwargs['summary']

    location = kwargs['location'].lower()

    levels = kwargs['levels']

    programs = []

    for program in kwargs['programs']:
        uw_program = Program.get_program(program)
        if uw_program:
            programs.append(uw_program)
        else:
            logger.error(COMPONENT, 'Error processing program: {}'.format(program))

    openings = 0

    try:
        if kwargs['openings']:
            openings = int(kwargs['openings']) or 0
    except Exception:
        pass

    index = False

    if index in kwargs:
        index = kwargs['index']

    job = Job.objects(id=kwargs['id']).first()

    remaining = job.openings

    # Job posting has decreased, some positions filled up
    if openings < job.openings:
        remaining = openings

    filtered_summary = engine.filter_summary(summary)

    summary_keywords = engine.get_keywords(filtered_summary, programs)

    filtered_summary_compare = re.sub(r'\W+', '', filtered_summary.lower().strip()).strip()
    job_summary_compare = re.sub(r'\W+', '', job.summary.lower().strip()).strip()

    employer = Employer.objects(jobs=kwargs['id']).first()

    # Job summary is not the same. In this case the employer most likely changed the job
    if not filtered_summary_compare == job_summary_compare:

        if openings >= 1:
            logger.info(COMPONENT, 'Job: {}: different summary detected, deprecating and creating new job..'
                        .format(kwargs['id']))

            job.update(set__deprecated=True)

            location = Location(name=location)

            keywords = [Keyword(keyword=k['keyword'], types=k['types']) for k in summary_keywords]

            # Assume new job so number of remaining positions is same as openings
            new_job = Job(title=job.title, summary=filtered_summary, year=job.year, term=job.term,
                          location=[location], openings=openings, remaining=openings,
                          levels=levels, programs=programs, url=job.url, keywords=keywords)

            new_job.save()

            employer.update(push__jobs=new_job)

            if index:
                elastic.delete_employer_jobmine(employer)
                elastic.delete_job_jobmine(employer, job)
                elastic.index_employer_jobmine(employer)
                elastic.index_job_jobmine(employer, new_job)
        else:
            logger.info(COMPONENT, 'Job: {}: different summary detected but invalid openings: {}, ignoring..'
                        .format(job.title, openings))
    else:
        logger.info(COMPONENT, 'Job: {}: updating for current term'.format(kwargs['id']))

        location = Location(name=location)

        job.update(add_to_set__location=location, set__remaining=remaining,
                   set__levels=list(set(levels + job.levels)),
                   set__programs=list(set(programs + job.programs)), set__last_indexed=datetime.now())

        if index:
            elastic.update_job_jobmine(employer, job)


def import_comment(**kwargs):
    """Import comment from RateMyCoopJob.

    Keyword arguments:
    employer_name -- Employer name
    job_title -- Title of job
    comments: -- Array of comments
        comment -- Comment
        comment_date -- Date comment was submitted. Note: in non-standard form such as: 5 years ago, 3 weeks ago etc
        salary -- Job salary (hourly)
        rating -- Job rating out of 5 (1 - 5 stars on ratemycoopjob)
    """

    employer_name = kwargs['employer_name'].lower()

    job_title = kwargs['job_title'].lower()

    # If employer alias exists (ex. Research in motion -> Blackberry), use instead
    if employer_name in employer_alias.aliases:
        employer_name = employer_alias.aliases[employer_name].lower()

    # If employer does not exist
    if not Employer.objects.search_text("\"{}\"".format(employer_name)).count() > 0:
        logger.info(COMPONENT, 'Employer: {} does not exist, ignoring..'.format(employer_name))
        return

    logger.info(COMPONENT, 'Importing comments for job: {} from employer: {}'.format(job_title, employer_name))

    employer = Employer.objects.search_text("\"{}\"".format(employer_name)).no_dereference().first()

    # Iterate through all comments
    for index, comment_obj in enumerate(kwargs['comments']):

        comment = comment_obj['comment']

        comment_date = _get_comment_date(comment_obj['comment_date'])

        salary = float(comment_obj['salary'])

        rating = float(comment_obj['rating']) / 5

        # If job does not exist add to employer
        if not employer.job_exists(job_title):
            if employer.comment_exists(comment=comment, date=comment_date, salary=salary, rating=rating):
                logger.info(COMPONENT, 'Comment: {} already exists for employer: {}, ignoring'
                            .format(index, employer_name))

            else:
                logger.info(COMPONENT, 'Adding comment: {} to employer: {}'.format(index, employer_name))

                new_comment = Comment(comment=comment, date=comment_date, salary=salary, crawled=True,
                                      rating=AggregateRating(rating=rating, count=1))

                employer.update(push__comments=new_comment)

        # Job already exists
        else:
            job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

            if job.comment_exists(comment=comment, date=comment_date, salary=salary, rating=rating):
                logger.info(COMPONENT, 'Comment: {} already exists for job: {} for employer: {}, ignoring'
                            .format(index, job_title, employer_name))

            else:
                logger.info(COMPONENT, 'Adding comment: {} for job: {} from {}'.format(index, job_title, employer_name))

                new_comment = Comment(comment=comment, date=comment_date, salary=salary, crawled=True,
                                      rating=AggregateRating(rating=rating, count=1))

                job.update(push__comments=new_comment)


def _get_comment_date(date_str):
    now = datetime.now()

    date = datetime(now.year, now.month, now.day)

    date_re = re.search(r'(\d+)\s(month[s]?|year[s]?|day[s]?)', date_str)

    # Ex. for 5 days ago, date_num = 5
    date_num = int(date_re.group(1))

    # Ex. for 5 days ago, date_time = days
    date_time = date_re.group(2)

    if 'day' in date_time:
        if date_num < 1:
            date_num = 1

        date -= relativedelta(days=date_num)

    elif 'month' in date_time:
        if date_num < 1:
            date_num = 1

        date -= relativedelta(months=date_num)

    elif 'year' in date_time:
        date -= relativedelta(years=date_num)

    return date
