from datetime import datetime
import mongoengine

import elasticsearch
from elasticsearch import helpers

from models.employer import Employer
import models.term as Term

import shared.secrets as secrets
import shared.logger as logger


COMPONENT = 'Search'

elastic_instance = elasticsearch.Elasticsearch()


def index_employer_waterlooworks(employer):
    employer_document = {
        "_index": "waterlooworks",
        "_type": "employers",
        "_id": employer.name,
        "_source": {
            "employer_name": employer.name,
            "employer_jobs": [str(job.id) for job in employer.jobs]
        }
    }

    elastic_instance.index('waterlooworks', 'employers', employer_document, id=employer.name)


def update_employer_waterlooworks(employer):
    employer_document = {
        "doc": {
            "employer_name": employer.name,
            "employer_jobs": [str(job.id) for job in employer.jobs]
        }
    }

    elastic_instance.update('waterlooworks', 'employers', employer.name, body=employer_document)


def delete_employer_waterlooworks(employer):
    elastic_instance.delete('waterlooworks', 'employers', employer.name, ignore=[404])


def index_job_waterlooworks(employer, job):
    job_document = {
        "_index": "waterlooworks",
        "_type": "jobs",
        "_parent": employer.name,
        "_id": str(job.id),
        "_source": {
            "employer_name": employer.name,
            "job_title": job.title,
            "job_year": job.year,
            "job_term": job.term,
            "job_summary": job.summary,
            "job_keywords": [k.keyword for k in job.keywords],
            "job_locations": [location.name for location in job.location],
            "job_programs": job.programs,
            "job_levels": job.levels
        }
    }

    elastic_instance.index('waterlooworks', 'jobs', job_document, id=str(job.id), parent=employer.name)


def update_job_waterlooworks(employer, job):
    job_document = {
        "doc": {
            "employer_name": employer.name,
            "job_title": job.title,
            "job_year": job.year,
            "job_term": job.term,
            "job_summary": job.summary,
            "job_keywords": [k.keyword for k in job.keywords],
            "job_locations": [location.name for location in job.location],
            "job_programs": job.programs,
            "job_levels": job.levels
        }
    }

    elastic_instance.update('waterlooworks', 'jobs', str(job.id), body=job_document, parent=employer.name)


def delete_job_waterlooworks(employer, job):
    elastic_instance.delete('waterlooworks', 'job', str(job.id), parent=employer.name, ignore=[404])


def index_waterlooworks():
    logger.info(COMPONENT, 'Indexing waterlooworks data')

    elastic_instance.indices.delete(index='waterlooworks', ignore=[404])

    elastic_instance.indices.create('waterlooworks', body={
        "mappings": {
            "employers": {
                "properties": {
                    "employer_name": {"type": "string"},
                    "employer_jobs": {"type": "string"}
                }
            },
            "jobs": {
                "_parent": {
                    "type": "employers"
                },
                "properties": {
                    "job_title": {"type": "string"},
                    "job_year": {"type": "integer"},
                    "job_term": {"type": "string"},
                    "job_summary": {"type": "string"},
                    "job_locations": {"type": "string"},
                    "job_programs": {"type": "string"},
                    "job_levels": {"type": "string"}
                }
            }
        }
    })

    logger.info(COMPONENT, 'Indexing waterlooworks employers and jobs')

    employers = []
    jobs = []

    for employer in Employer.objects.only('name', 'jobs'):
        logger.info(COMPONENT, 'Indexing employer: {}'.format(employer.name))

        employer_document = {
            "_index": "waterlooworks",
            "_type": "employers",
            "_id": employer.name,
            "_source": {
                "employer_name": employer.name,
                "employer_jobs": [str(job.id) for job in employer.jobs]
            }
        }

        employers.append(employer_document)

        for job in employer.jobs:
            if not job.deprecated:
                logger.info(COMPONENT, 'Indexing job: {} for employer: {}'.format(job.title, employer.name))

                job_document = {
                    "_index": "waterlooworks",
                    "_type": "jobs",
                    "_parent": employer.name,
                    "_id": str(job.id),
                    "_source": {
                        "employer_name": employer.name,
                        "job_title": job.title,
                        "job_year": job.year,
                        "job_term": job.term,
                        "job_summary": job.summary,
                        "job_keywords": [k.keyword for k in job.keywords],
                        "job_locations": [location.name for location in job.location],
                        "job_programs": job.programs,
                        "job_levels": job.levels
                    }
                }

                jobs.append(job_document)

            if len(jobs) == 1000:
                helpers.bulk(elastic_instance, jobs)
                jobs = []

        if len(employers) == 1000:
            helpers.bulk(elastic_instance, employers)
            employers = []

    if len(employers) > 0:
        helpers.bulk(elastic_instance, employers)

    if len(jobs) > 0:
        helpers.bulk(elastic_instance, jobs)


def query_jobs_and_employers(query, page):
    start_page = 10 * (int(page) - 1)

    now = datetime.now()

    response = elastic_instance.search(index='waterlooworks', doc_type=['jobs'], body={
        "from": start_page, "size": 10,
        "sort": [
            {"job_year": "desc"},
            "_score"
        ],
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "job_term": Term.get_term(now.month)
                        }
                    }
                ],
                "must": {
                    "multi_match": {
                        "query": query,
                        "type": "cross_fields",
                        "fields": ["employer_name^4", "job_title^4", "job_term"]
                    }
                }
            }
        }
    })

    return response


def query_jobs(query, page):
    start_page = 10 * (int(page) - 1)

    now = datetime.now()

    body = {
        "from": start_page, "size": 10,
        "sort": [
            {"job_year": "desc"},
            "_score"
        ],
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "job_term": Term.get_term(now.month)
                        }
                    }
                ]
            }
        }
    }

    if query:
        body['query']['bool']['must'] = {
            "multi_match": {
                "query": query,
                "type": "cross_fields",
                "fields": ["job_title^4", "job_keywords^4", "job_summary^3", "job_term"]
            }
        }

    response = elastic_instance.search(index='waterlooworks', doc_type=['jobs'], body=body)

    return response


if __name__ == "__main__":
    mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)
    index_waterlooworks()
