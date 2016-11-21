import mongoengine
import elasticsearch
from elasticsearch import helpers

from models.employer import Employer

import shared.secrets as secrets
import shared.logger as logger


COMPONENT = 'Elastic'

mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)

elastic = elasticsearch.Elasticsearch()


def index_jobmine():
    logger.info(COMPONENT, 'Indexing jobmine data')

    elastic.indices.delete(index='jobmine', ignore=[404])

    elastic.indices.create('jobmine', body={
        "mappings": {
            "employers": {
                "properties": {
                    "name": {"type": "string"},
                    "jobs": {"type": "string"}
                }
            },
            "jobs": {
                "_parent": {
                    "type": "employers"
                },
                "properties": {
                    "title": {"type": "string"},
                    "year": {"type": "integer"},
                    "term": {"type": "string"},
                    "summary": {"type": "string"},
                    "locations": {"type": "string"},
                    "programs": {"type": "string"},
                    "levels": {"type": "string"}
                }
            }
        }
    })

    logger.info(COMPONENT, 'Indexing jobmine employers and jobs')

    employers = []
    jobs = []

    job_index = 0

    for i, employer in enumerate(Employer.objects.only('name', 'jobs')):
        logger.info(COMPONENT, 'Indexing employer: {}'.format(employer.name))

        employer_document = {
            "_index": "jobmine",
            "_type": "employers",
            "_id": i,
            "_source": {
                "name": employer.name,
                "jobs": [job.title for job in employer.jobs]
            }
        }

        employers.append(employer_document)

        for job in employer.jobs:
            logger.info(COMPONENT, 'Indexing job: {} for employer: {}'.format(job.title, employer.name))

            job_document = {
                "_index": "jobmine",
                "_type": "jobs",
                "_parent": i,
                "_id": job_index,
                "_source": {
                    "title": job.title,
                    "year": job.year,
                    "term": job.term,
                    "summary": job.term,
                    "locations": [location.name for location in job.location],
                    "programs": job.programs,
                    "levels": job.levels
                }
            }

            jobs.append(job_document)

            job_index += 1

            if len(jobs) == 1000:
                helpers.bulk(elastic, jobs)
                jobs = []

        if len(employers) == 1000:
            helpers.bulk(elastic, employers)
            employers = []

    if len(employers) > 0:
        helpers.bulk(elastic, employers)

    if len(jobs) > 0:
        helpers.bulk(elastic, jobs)


if __name__ == "__main__":
    index_jobmine()
