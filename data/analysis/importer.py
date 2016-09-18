from mongoengine import *

from models.employer import Employer
from models.job import Job


def import_job(employer_name, job_title, summary, year, term, location, openings, remaining=None, applicants=0):
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
    applicants = int(applicants)

    if remaining is not None:
        remaining = int(remaining)

    # If employer does not exist, create it
    if not Employer.employer_exists(employer_name):
        employer = Employer(name=employer_name)

        job = Job(title=job_title.lower(), summary=summary, year=year, term=term, location=location.lower(),
                  openings=openings, remaining=remaining, applicants=[applicants])

        employer.jobs.append(job)
        employer.save()

    # Employer already exists
    else:
        employer = Employer.objects(name=employer_name).no_dereference().first()

        # If job does not exist, create it
        if not Job.job_exists(job_title):
            job = Job(title=job_title.lower(), summary=summary, year=year, term=term, location=location.lower(),
                      openings=openings, remaining=remaining, applicants=[applicants])

            employer.jobs.append(job)
            employer.save()

        # Job already exists
        else:
            job = Job.objects(_id__in=employer.jobs, title=job_title).first()

            # Check if job is 'same'

#            if summary.strip() == job.summary.strip() :
































