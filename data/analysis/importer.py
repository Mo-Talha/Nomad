from mongoengine import *

from datetime import datetime

from models.employer import Employer
from models.job import Job
from models.applicant import Applicant

import engine
import filters


def import_job(**kwargs):
    """Import job from Jobmine.

    Keyword arguments:
    employer_name -- Employer name
    job_title -- Title of job
    year -- Year the job was advertised
    term -- Term job was advertised [Fall -> 1, Winter -> 2, Spring -> 3]
    location -- Location job was advertised
    openings -- Number of job openings
    remaining -- Number of job openings remaining
    summary -- Job summary
    """

    # Convert to ASCII (ignore Unicode)
    employer_name = kwargs['employer_name'].encode('ascii', 'ignore')
    job_title = kwargs['job_title'].encode('ascii', 'ignore')
    year = int(kwargs['year'])
    term = int(kwargs['term'])
    location = kwargs['location'].encode('ascii', 'ignore')
    openings = int(kwargs['openings'])
    summary = kwargs['summary']

    applicants = 0

    if not kwargs['applicants'].encode('ascii', 'ignore'):
        applicants = int(kwargs['applicants'])

    # If employer does not exist, create it
    if not Employer.employer_exists(employer_name):
        employer = Employer(name=employer_name)

        applicant = Applicant(applicants=applicants, date=datetime.now())

        # Assume new job so number of remaining positions is same as openings
        job = Job(title=job_title.lower(), summary=engine.filter_summary(summary), year=year, term=term,
                  location=location.lower(), openings=openings, remaining=openings, applicants=[applicant])

        job.save()

        employer.jobs.append(job)
        employer.save()

    # Employer already exists
    else:
        employer = Employer.objects(name=employer_name).no_dereference().first()

        # If job does not exist, create it
        if not Job.job_exists(job_title):
            applicant = Applicant(applicants=applicants, date=datetime.now())

            # Assume new job so number of remaining positions is same as openings
            job = Job(title=job_title.lower(), summary=engine.filter_summary(summary), year=year, term=term,
                      location=location.lower(), openings=openings, remaining=openings, applicants=[applicant])

            job.save()

            employer.jobs.append(job)
            employer.save()

        # Job already exists
        else:
            job = Job.objects(_id__in=employer.jobs, title=job_title).first()

            filtered_summary = engine.filter_summary(summary)

            # Check if job is 'same'
