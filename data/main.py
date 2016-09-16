from mongoengine import *

import analysis.importer as importer
import data.crawler.jobmine.jobmine_crawler as jobmine
import shared.secrets as secrets


def connect():
    connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST,
            port=secrets.MONGO_PORT)

if __name__ == '__main__':
    connect()

    jobmine_crawler = jobmine.JobmineCrawler(importer)
    jobmine_crawler.run()
