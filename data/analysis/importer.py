from mongoengine import *

import shared.constants as constants


def import_job(employer, job_title, year, term, location, openings, remaining, summary):
    """Import job from Jobmine.

    Keyword arguments:
    employer -- Employer name
    job_title -- Title of job
    year -- Year the job was advertised
    term -- Term job was advertised [Fall -> 1, Winter -> 2, Spring -> 3]
    location -- Location job was advertised
    openings -- Number of job openings
    remaining -- Number of job openings remaining
    summary -- Job summary
    """

    if not employer:
        raise AttributeError("Employer attribute cannot be empty")

    if not job_title:
        raise AttributeError("Job title attribute cannot be empty")

    if not year:
        raise AttributeError("Year attribute cannot be empty")

    if term not in [constants.FALL_TERM, constants.WINTER_TERM, constants.SPRING_TERM]:
        raise AttributeError("Term attribute: {} is invalid".format(term))

    if not location:
        raise AttributeError("Location attribute cannot be empty")

    if not openings >= 1:
        raise AttributeError("Openings attribute: {} must be greater than 1".format(openings))

    if not remaining >= 1:
        raise AttributeError("Remaining attribute: {} must be greater than 1".format(remaining))

    if remaining > openings:
        raise AttributeError("Remaining attribute: {} must less than or equal to openings: {}"
                             .format(remaining, openings))

    if not summary:
        raise AttributeError("Summary attribute cannot be empty")

    
