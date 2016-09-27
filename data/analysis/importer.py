from mongoengine import *

from datetime import datetime
import re

from models.exceptions import DataIntegrityError
import shared.logger as logger

from models.employer import Employer
from models.job import Job
from models.applicant import Applicant
from models.comment import Comment

import models.program as Program

import engine

COMPONENT = 'Importer'


def import_job(**kwargs):
    """Import job from Jobmine.

    Keyword arguments:
    employer_name -- Employer name
    job_title -- Title of job
    year -- Year the job was advertised
    term -- Term job was advertised [Fall -> 1, Winter -> 2, Spring -> 3]
    levels -- Levels job is intended for [Junior, Intermediate, Senior]
    programs -- Programs the job is specified for
    location -- Location job was advertised
    openings -- Number of job openings
    remaining -- Number of job openings remaining
    summary -- Job summary
    """

    # Convert to ASCII (ignore Unicode)
    employer_name = kwargs['employer_name'].encode('ascii', 'ignore').lower()
    job_title = kwargs['job_title'].encode('ascii', 'ignore').lower()
    term = int(kwargs['term'])

    levels = [level.encode('ascii', 'ignore').strip() for level in kwargs['levels'].split(',')]

    programs = [Program.get_program(program.encode('ascii', 'ignore').strip())
                for program in kwargs['programs'].split(',')]

    location = kwargs['location'].encode('ascii', 'ignore').lower()
    openings = int(kwargs['openings'])
    summary = kwargs['summary']
    date = kwargs['date']
    year = date.year

    applicants = 0

    if kwargs['applicants'].encode('ascii', 'ignore'):
        applicants = int(kwargs['applicants'])

    logger.info(COMPONENT, 'Importing job: {} from {}'.format(job_title, employer_name))

    # If employer does not exist, create it
    if not Employer.employer_exists(employer_name):
        logger.info(COMPONENT, 'Employer: {} does not exist, creating..'.format(employer_name))

        employer = Employer(name=employer_name)

        applicant = Applicant(applicants=applicants, date=date)

        logger.info(COMPONENT, 'Creating job: {}..'.format(job_title))

        # Assume new job so number of remaining positions is same as openings
        job = Job(title=job_title, summary=engine.filter_summary(summary).encode('ascii', 'ignore'), year=year,
                  term=term, location=[location], openings=openings, remaining=openings, applicants=[applicant],
                  levels=levels, programs=programs)

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

            # Assume new job so number of remaining positions is same as openings
            job = Job(title=job_title, summary=engine.filter_summary(summary).encode('ascii', 'ignore'), year=year,
                      term=term, location=[location], openings=openings, remaining=openings, applicants=[applicant],
                      levels=levels, programs=programs)

            job.save()

            employer.update(push__jobs=job)

        # Job already exists
        else:
            logger.info(COMPONENT, 'Job: {} already exists'.format(job_title))

            job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()
    
            filtered_summary = engine.filter_summary(summary).encode('ascii', 'ignore')

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
                              levels=levels, programs=programs)
    
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
                    
                    job.update(set__year=year, set__term=term, add_to_set__location=location, set__openings=openings,
                               set__remaining=openings, push__applicants=Applicant(applicants=applicants, date=date),
                               set__levels=levels, set__programs=programs)

                # Job is being updated. We need to update location, openings, levels, remaining, hire_rate, applicants
                else:
                    logger.info(COMPONENT, 'Job: {}: updating for current term'.format(job_title))

                    remaining = job.openings

                    # Job posting has decreased, some positions filled up
                    if openings < job.openings:
                        remaining = openings

                    job.update(add_to_set__location=location, set__remaining=remaining,
                               push__applicants=Applicant(applicants=applicants, date=date),
                               set__levels=list(set(levels + job.levels)),
                               set__programs=list(set(programs + job.programs)))


def import_comment(**kwargs):
    """Import comment from RateMyCoopJob.

    Keyword arguments:
    employer_name -- Employer name
    job_title -- Title of job
    comment -- Comment
    comment_date -- Date comment was submitted. Note: in non-standard form such as: 5 years ago, 3 weeks ago
    salary -- Job salary (hourly)
    rating -- Job rating out of 5
    """

    # Convert to ASCII (ignore Unicode)
    employer_name = kwargs['employer_name'].encode('ascii', 'ignore').lower()
    job_title = kwargs['job_title'].encode('ascii', 'ignore').lower()
    comment = kwargs['comment'].encode('ascii', 'ignore')
    comment_date = _get_comment_date(kwargs['comment_date'].encode('ascii', 'ignore'))
    salary = float(kwargs['salary'])
    rating = float(kwargs['rating']) / 5

    logger.info(COMPONENT, 'Importing comment for job: {} from {}'.format(job_title, employer_name))

    # If employer does not exist
    if not Employer.employer_exists(employer_name):
        logger.info(COMPONENT, 'Employer: {} does not exist, ignoring..'.format(employer_name))

    # Employer already exists
    else:
        employer = Employer.objects(name=employer_name).no_dereference().first()

        logger.info(COMPONENT, 'Employer: {} exists'.format(employer_name))

        # If job does not exist
        if not employer.job_exists(job_title):
            logger.info(COMPONENT, 'Job: {} does not exist, ignoring..'.format(job_title))

        # Job already exists
        else:
            logger.info(COMPONENT, 'Job: {} exists'.format(job_title))

            job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

            # If comment does not exist
            if job.comment_exists(comment):
                logger.info(COMPONENT, 'Comment already exists for job: {}, ignoring..'.format(job_title))

            else:
                logger.info(COMPONENT, 'Job: {}: adding new comment'.format(job_title))

                new_comment = Comment(comment=comment, comment_date=comment_date, salary=salary, crawled=True)
                new_comment.rating.add_rating(rating)
                new_comment.save()


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
        month = date.month - date_num

    elif 'year' in date_time:
        year = date.year - date_num

    return datetime(year, month, day)


