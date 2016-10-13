from datetime import datetime
import re

import engine

from models.exceptions import DataIntegrityError
from models.employer import Employer
from models.job import Job
from models.applicant import Applicant
from models.comment import Comment
from models.keyword import Keyword
import models.employer_alias as employer_alias

import models.program as Program

import shared.logger as logger


COMPONENT = 'Importer'


def import_job(**kwargs):
    """Import job from Jobmine.

    Keyword arguments:
    employer_name -- Employer name
    job_title -- Title of job
    summary -- Job summary
    year -- Year the job was advertised
    term -- Term job was advertised [Fall -> 1, Winter -> 2, Spring -> 3]
    location -- Location job was advertised
    openings -- Number of job openings
    remaining -- Number of job openings remaining
    applicants -- Number of applicants job has (Optional)
    levels -- Levels job is intended for [Junior, Intermediate, Senior]
    programs -- Programs the job is specified for
    url -- URL of job in Jobmine (Optional)
    date -- Date job was crawled (useful for knowing exactly # of applicants at what time)
    """

    employer_name = kwargs['employer_name'].encode('ascii', 'ignore').lower()

    job_title = kwargs['job_title'].encode('ascii', 'ignore').lower()

    term = int(kwargs['term'])

    levels = [level.encode('ascii', 'ignore').strip() for level in kwargs['levels'].split(',')]

    programs = [Program.get_program(program.encode('ascii', 'ignore').strip())
                for program in kwargs['programs'].split(',')]

    location = kwargs['location'].encode('ascii', 'ignore').lower()

    openings = int(kwargs['openings'])

    summary = kwargs['summary']

    filtered_summary = engine.filter_summary(summary)

    summary_keywords = engine.get_keywords(summary, programs)

    keywords = []

    for keyword in summary_keywords:
        keywords.append(Keyword(keyword='', type=''))

    date = kwargs['date']
    year = date.year

    applicants = 0

    if 'applicants' in kwargs and (isinstance(kwargs['applicants'], str) or
                                   isinstance(kwargs['applicants'], unicode) and kwargs['applicants'].strip()):
        applicants = int(kwargs['applicants'])

    url = None

    if 'url' in kwargs:
        url = kwargs['url']

    logger.info(COMPONENT, 'Importing job: {} from {}'.format(job_title, employer_name))

    # If employer does not exist, create it
    if not Employer.employer_exists(employer_name):
        logger.info(COMPONENT, 'Employer: {} does not exist, creating..'.format(employer_name))

        employer = Employer(name=employer_name)

        logger.info(COMPONENT, 'Creating job: {}..'.format(job_title))

        applicant = Applicant(applicants=applicants, date=date)

        # New job so number of remaining positions is same as openings
        job = Job(title=job_title, summary=filtered_summary, year=year,
                  term=term, location=[location], openings=openings, remaining=openings,
                  applicants=[applicant], levels=levels, programs=programs, url=url,
                  keywords=keywords)

        job.save()

        employer.jobs.append(job)
        employer.save()

    # Employer already exists
    else:
        employer = Employer.objects(name=employer_name).no_dereference().first()

        logger.info(COMPONENT, 'Employer: {} already exists'.format(employer_name))

        # If job does not exist, create it
        if not employer.job_exists(job_title):
            logger.info(COMPONENT, 'Creating job: {}..'.format(job_title))

            applicant = Applicant(applicants=applicants, date=date)

            # New job so number of remaining positions is same as openings
            job = Job(title=job_title, summary=engine.filter_summary(summary), year=year,
                      term=term, location=[location], openings=openings, remaining=openings,
                      applicants=[applicant], levels=levels, programs=programs, url=url,
                      keywords=keywords)

            job.save()

            employer.update(push__jobs=job)

        # Job already exists
        else:
            logger.info(COMPONENT, 'Job: {} already exists'.format(job_title))

            job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

            if not year >= job.year:
                raise DataIntegrityError('Job: {} by {} cannot be advertised before {}'
                                         .format(job_title, employer_name, job.year))

            # Job summary is not the same. In this case the employer most likely changed the job
            if not filtered_summary == job.summary:
                logger.info(COMPONENT, 'Job: {}: different summary detected, deprecating and creating new job..'
                            .format(job_title))

                job.update(set__deprecated=True)
                
                applicant = Applicant(applicants=applicants, date=date)
    
                # Assume new job so number of remaining positions is same as openings
                new_job = Job(title=job_title, summary=filtered_summary, year=year, term=term,
                              location=[location], openings=openings, remaining=openings, applicants=[applicant],
                              levels=levels, programs=programs, url=url, keywords=keywords)
    
                new_job.save()
    
                employer.update(push__jobs=new_job)
            
            # Job is the same (same title and description)
            else:
                # If job is being advertised in new term
                if year != job.year or term != job.term:
                    logger.info(COMPONENT, 'Job: {}: being advertised in new term, updating..'.format(job_title))

                    # Add hire ratio for previous term
                    hire_ratio = float(job.openings - job.remaining) / job.openings
                    
                    job.hire_rate.add_rating(hire_ratio)

                    applicant = Applicant(applicants=applicants, date=date)
                    
                    job.update(set__year=year, set__term=term, add_to_set__location=location, set__openings=openings,
                               set__remaining=openings, push__applicants=applicant,
                               set__levels=levels, set__programs=programs, url=url)

                # Job is being updated. We need to update location, openings, levels, remaining, hire_rate, applicants
                else:
                    logger.info(COMPONENT, 'Job: {}: updating for current term'.format(job_title))

                    remaining = job.openings

                    # Job posting has decreased, some positions filled up
                    if openings < job.openings:
                        remaining = openings

                    applicant = Applicant(applicants=applicants, date=date)

                    job.update(add_to_set__location=location, set__remaining=remaining,
                               set__levels=list(set(levels + job.levels)), push__applicants=applicant,
                               set__programs=list(set(programs + job.programs)), url=url)


def update_job(**kwargs):
    """Update job from Jobmine.

    Keyword arguments:
    id -- Job ID
    summary -- Job summary
    location -- Location job was advertised
    programs -- Programs the job is specified for
    levels -- Levels job is intended for [Junior, Intermediate, Senior]
    openings -- Number of job openings
    """

    summary = kwargs['summary']

    location = kwargs['location'].encode('ascii', 'ignore').lower()

    programs = [Program.get_program(program.encode('ascii', 'ignore').strip())
                for program in kwargs['programs'].split(',')]

    levels = [level.encode('ascii', 'ignore').strip() for level in kwargs['levels'].split(',')]

    openings = int(kwargs['openings'])

    job = Job.objects(id=kwargs['id']).first()

    remaining = job.openings

    # Job posting has decreased, some positions filled up
    if openings < job.openings:
        remaining = openings

    filtered_summary = engine.filter_summary(summary)

    # Job summary is not the same. In this case the employer most likely changed the job
    if not filtered_summary == job.summary:
        logger.info(COMPONENT, 'Job: {}: different summary detected, deprecating and creating new job..'
                    .format(kwargs['id']))

        employer = Employer.objects(jobs=kwargs['id']).first()

        job.update(set__deprecated=True)

        # Assume new job so number of remaining positions is same as openings
        new_job = Job(title=job.title, summary=filtered_summary, year=job.year, term=job.term,
                      location=[location], openings=openings, remaining=openings,
                      levels=levels, programs=programs, url=job.url)

        new_job.save()

        employer.update(push__jobs=new_job)

    else:
        logger.info(COMPONENT, 'Job: {}: updating for current term'.format(kwargs['id']))

        job.update(add_to_set__location=location, set__remaining=remaining,
                   set__levels=list(set(levels + job.levels)),
                   set__programs=list(set(programs + job.programs)))


def import_comment(**kwargs):
    """Import comment from RateMyCoopJob.

    Keyword arguments:
    employer_name -- Employer name
    job_title -- Title of job
    comments: -- Array of comments
        comment -- Comment
        comment_date -- Date comment was submitted. Note: in non-standard form such as: 5 years ago, 3 weeks ago etc
        salary -- Job salary (hourly)
        rating -- Job rating out of 5
    """

    employer_name = kwargs['employer_name'].encode('ascii', 'ignore').lower()

    job_title = kwargs['job_title'].encode('ascii', 'ignore').lower()

    # If employer alias exists (ex. Research in motion -> Blackberry), use instead
    if employer_name in employer_alias.aliases:
        employer_name = employer_alias.aliases[employer_name]

    # If employer does not exist
    if not Employer.objects.search_text("\"{}\"".format(employer_name)).count() > 0:
        logger.info(COMPONENT, 'Employer: {} does not exist, ignoring..'.format(employer_name))
        return

    logger.info(COMPONENT, 'Importing comments for job: {} from {}'.format(job_title, employer_name))

    employer = Employer.objects.search_text(employer_name).no_dereference().first()

    # Iterate through all comments
    for index, comment_obj in enumerate(kwargs['comments']):

        comment = comment_obj['comment'].encode('ascii', 'ignore')

        comment_date = _get_comment_date(comment_obj['comment_date'])

        salary = float(comment_obj['salary'])

        rating = float(comment_obj['rating']) / 5

        # If job does not exist
        if not employer.job_exists(job_title):
            if employer.comment_exists(comment):
                logger.info(COMPONENT, 'Comment: {} already exists for employer: {}, ignoring..'
                            .format(index, employer_name))

            else:
                logger.info(COMPONENT, 'Adding comment: {} to employer: {}'.format(index, employer_name))

                new_comment = Comment(title=job_title, comment=comment, date=comment_date, salary=salary, crawled=True)
                new_comment.rating.add_rating(rating)

                employer.update(push__comments=new_comment)

        # Job already exists
        else:
            job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

            if job.comment_exists(comment):
                logger.info(COMPONENT, 'Comment: {} already exists for job: {}, ignoring..'.format(index, job_title))

            else:
                logger.info(COMPONENT, 'Adding comment: {} for job: {} from {}'.format(index, job_title, employer_name))

                new_comment = Comment(comment=comment, date=comment_date, salary=salary, crawled=True)
                new_comment.rating.add_rating(rating)

                job.update(push__comments=new_comment)

                # Remove same comment from employer (if exists)
                logger.info(COMPONENT, 'Removing redundant comment: {} from employer {}'.format(index, employer_name))

                employer.get_crawled_comments(comment).delete()


def _get_comment_date(date_str):
    date = datetime.now()

    date_re = re.search(r'(\d+)\s(month[s]?|year[s]?|day[s]?)', date_str)

    # Ex. for 5 days ago, date_num = 5
    date_num = int(date_re.group(1))

    # Ex. for 5 days ago, date_time = days
    date_time = date_re.group(2)

    day, month, year = date.day, date.month, date.year

    if 'day' in date_time:
        day = date.day - date_num

    elif 'month' in date_time:
        if datetime == 12:
            year = date.year - 1

        else:
            month = date.month - date_num

    elif 'year' in date_time:
        year = date.year - date_num

    if day < 1:
        day = 1

    if not 1 <= month <= 12:
        month = 1

    return datetime(year, month, day)
