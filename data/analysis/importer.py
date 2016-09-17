from mongoengine import *

from models.employer import Employer
from models.job import Job

import shared.constants as constants


def import_job(employer_name, job_title, summary, year, term, location, openings, remaining=None):
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

    # Convert to ASCII (ignore Unicode) and int
    employer_name = employer_name.encode('ascii', 'ignore')
    job_title = job_title.encode('ascii', 'ignore')
    summary = summary.encode('ascii', 'ignore')
    year = int(year)
    term = int(term)
    location = location.encode('ascii', 'ignore')
    openings = int(openings)

    if remaining is not None:
        remaining = int(remaining)

    if not Employer.employer_exists(employer_name):
        employer = Employer(name=employer_name)

        job = Job(title=job_title.lower(), summary=summary, year=year, term=term, location=location,
                  openings=openings, remaining=remaining)

        employer.jobs.append(job)
        job.save()

        employer.save()


