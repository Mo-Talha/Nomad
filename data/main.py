import sys

import mongoengine

from data.crawler.jobmine.jobmine_crawler import JobmineCrawler
from data.crawler.ratemycoopjob.ratemycoopjob_crawler import RateMyCoopJobCrawler

import shared.secrets as secrets


def connect_mongo():
    mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)

if __name__ == '__main__':
    connect_mongo()

    if len(sys.argv) > 1:
        if sys.argv[1] == 'jobmine':
            jobmine_crawler = JobmineCrawler()
            jobmine_crawler.run()

        elif sys.argv[1] == 'ratemycoopjob':
            ratemycoopjob_crawler = RateMyCoopJobCrawler()
            ratemycoopjob_crawler.run()

    else:
        jobmine_crawler = JobmineCrawler()
        jobmine_crawler.run()
