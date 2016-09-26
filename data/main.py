import sys

from mongoengine import *

import data.crawler.jobmine.jobmine_crawler as jobmine
import data.crawler.ratemycoopjob.ratemycoopjob_crawler as ratemycoopjob

import shared.secrets as secrets


def connect_mongo():
    connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST,
            port=secrets.MONGO_PORT)

if __name__ == '__main__':
    connect_mongo()

    if sys.argv[1]:
        if sys.argv[1] == 'jobmine':
            jobmine_crawler = jobmine.JobmineCrawler()
            jobmine_crawler.run()

        elif sys.argv[1] == 'ratemycoopjob':
            ratemycoopjob_crawler = ratemycoopjob.RateMyCoopJobCrawler()
            ratemycoopjob_crawler.run()

        else:
            jobmine_crawler = jobmine.JobmineCrawler()
            jobmine_crawler.run()
