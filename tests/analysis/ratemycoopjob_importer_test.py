import unittest
import time
import mongoengine

from datetime import datetime
from dateutil.relativedelta import relativedelta

import tests.analysis.importer_datamanager as datamanager
import data.analysis.importer as importer

from models.employer import Employer
from models.job import Job
import models.term as Term

import shared.secrets as secrets


mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)


class RateMyCoopJobImporterTest(unittest.TestCase):

    def setUp(self):
        self.employer_name = 'Test Employer 1'
        self.job_title = 'Test Job Title 1'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Toronto'
        job_levels = ['Junior', 'Intermediate', 'Senior']
        openings = 10
        applicants = 50
        summary = datamanager.test_summary
        programs = ['MATH-Computer Science', 'ENG-Computer', 'ENG-Civil']
        job_url = 'https://testurl.com'

        importer.import_job(employer_name=self.employer_name, job_title=self.job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        self.employer_name = self.employer_name.lower()
        self.job_title = self.job_title.lower()
        location = location.lower()

        self.employer = Employer.objects(name=self.employer_name).no_dereference().first()

        self.job = Job.objects(id__in=[job.id for job in self.employer.jobs], title=self.job_title).first()

        self.assertEqual(self.employer.name, self.employer_name)
        self.assertEqual(self.employer.overall.rating, 0.0)
        self.assertEqual(self.employer.overall.count, 0)
        self.assertTrue(len(self.employer.warnings) == 0)
        self.assertTrue(len(self.employer.comments) == 0)

        self.assertEqual(self.job.title, self.job_title)
        self.assertEqual(self.job.url, job_url)
        self.assertEqual(self.job.term, term)
        self.assertEqual(self.job.location[0].name, location)
        self.assertTrue(int(round(self.job.location[0].longitude)) == -79)
        self.assertTrue(int(round(self.job.location[0].latitude)) == 44)
        self.assertEqual(self.job.openings, openings)
        self.assertEqual(self.job.remaining, openings)
        self.assertEqual(self.job.hire_rate.rating, 0.0)
        self.assertEqual(self.job.hire_rate.count, 0)
        self.assertEqual(self.job.applicants[0].applicants, applicants)
        self.assertEqual(self.job.applicants[0].date.year, now.year)
        self.assertEqual(self.job.applicants[0].date.month, now.month)
        self.assertEqual(self.job.applicants[0].date.day, now.day)
        self.assertEqual(set(self.job.levels), set(job_levels))
        self.assertTrue(len(self.job.comments) == 0)
        self.assertEqual(set(self.job.programs), set(programs))
        self.assertFalse(self.job.deprecated)

        time.sleep(2)

    def tearDown(self):
        self.job.delete()
        self.employer.delete()

    def test_employer_does_not_exist_comments_import(self):
        comments = []

        comments.append({
            'comment': datamanager.test_comment_1,
            'comment_date': "5 days ago",
            'rating': 2,
            'salary': 17
        })

        importer.import_comment(employer_name="Test Comments Employer DNE", job_title=self.job_title, comments=comments)

        self.employer.reload()
        self.job.reload()

        job_comments = self.job.comments

        self.assertFalse(Employer.employer_exists('Test Comments Employer DNE'))
        self.assertTrue(len(job_comments) == 0)

    def test_employer_comments_import(self):
        comments = []

        comments.append({
            'comment': datamanager.test_comment_1,
            'comment_date': "5 days ago",
            'rating': 2,
            'salary': 17
        })

        comments.append({
            'comment': datamanager.test_comment_1,
            'comment_date': "5 days ago",
            'rating': 2,
            'salary': 17
        })

        comments.append({
            'comment': datamanager.test_comment_1,
            'comment_date': "7 day ago",
            'rating': 3,
            'salary': 17
        })

        importer.import_comment(employer_name=self.employer_name, job_title=self.job_title, comments=comments)

        self.employer.reload()
        self.job.reload()

        job_comments = self.job.comments
        now = datetime.now()
        date = datetime(now.year, now.month, now.day)

        self.assertTrue(len(self.employer.comments) == 0)
        self.assertTrue(len(job_comments) == 2)
        self.assertEquals(job_comments[0].comment, datamanager.test_comment_1)
        self.assertEquals(job_comments[0].date, date - relativedelta(days=5))
        self.assertEquals(job_comments[0].rating.rating, float(2) / 5)
        self.assertEquals(job_comments[0].rating.count, 1)
        self.assertEquals(job_comments[0].salary, 17)
        self.assertTrue(job_comments[0].crawled)

        self.assertEquals(job_comments[1].comment, datamanager.test_comment_1)
        self.assertEquals(job_comments[1].date, date - relativedelta(days=7))
        self.assertEquals(job_comments[1].rating.rating, float(3) / 5)
        self.assertEquals(job_comments[1].rating.count, 1)
        self.assertEquals(job_comments[1].salary, 17)
        self.assertTrue(job_comments[1].crawled)

        self.employer.comments.delete()
        self.job.comments.delete()

    def test_job_comments_import(self):
        comments = []

        comments.append({
            'comment': datamanager.test_comment_1,
            'comment_date': "5 days ago",
            'rating': 2,
            'salary': 17
        })

        comments.append({
            'comment': datamanager.test_comment_1,
            'comment_date': "5 days ago",
            'rating': 2,
            'salary': 17
        })

        comments.append({
            'comment': datamanager.test_comment_2,
            'comment_date': "1 day ago",
            'rating': 4,
            'salary': 19
        })

        comments.append({
            'comment': datamanager.test_comment_3,
            'comment_date': "4 months ago",
            'rating': 2,
            'salary': 25
        })

        comments.append({
            'comment': datamanager.test_comment_4,
            'comment_date': "7 months ago",
            'rating': 1,
            'salary': 22
        })

        comments.append({
            'comment': datamanager.test_comment_5,
            'comment_date': "12 months ago",
            'rating': 5,
            'salary': 20
        })

        comments.append({
            'comment': datamanager.test_comment_6,
            'comment_date': "3 years ago",
            'rating': 2,
            'salary': 50
        })

        comments.append({
            'comment': datamanager.test_comment_7,
            'comment_date': "1 year ago",
            'rating': 1,
            'salary': 1
        })

        comments.append({
            'comment': '',
            'comment_date': '15 month ago',
            'rating': 5,
            'salary': 100
        })
        
        importer.import_comment(employer_name=self.employer_name, job_title=self.job_title, comments=comments)

        self.employer.reload()
        self.job.reload()

        job_comments = self.job.comments
        now = datetime.now()
        date = datetime(now.year, now.month, now.day)

        self.assertTrue(len(job_comments) == 8)
        self.assertEquals(job_comments[0].comment, datamanager.test_comment_1)
        self.assertEquals(job_comments[0].date, date - relativedelta(days=5))
        self.assertEquals(job_comments[0].rating.rating, float(2) / 5)
        self.assertEquals(job_comments[0].rating.count, 1)
        self.assertEquals(job_comments[0].salary, 17)
        self.assertTrue(job_comments[0].crawled)

        self.assertEquals(job_comments[1].comment, datamanager.test_comment_2)
        self.assertEquals(job_comments[1].date, date - relativedelta(days=1))
        self.assertEquals(job_comments[1].rating.rating, float(4) / 5)
        self.assertEquals(job_comments[1].rating.count, 1)
        self.assertEquals(job_comments[1].salary, 19)
        self.assertTrue(job_comments[1].crawled)

        self.assertEquals(job_comments[2].comment, datamanager.test_comment_3)
        self.assertEquals(job_comments[2].date, date - relativedelta(months=4))
        self.assertEquals(job_comments[2].rating.rating, float(2) / 5)
        self.assertEquals(job_comments[2].rating.count, 1)
        self.assertEquals(job_comments[2].salary, 25)
        self.assertTrue(job_comments[2].crawled)

        self.assertEquals(job_comments[3].comment, datamanager.test_comment_4)
        self.assertEquals(job_comments[3].date, date - relativedelta(months=7))
        self.assertEquals(job_comments[3].rating.rating, float(1) / 5)
        self.assertEquals(job_comments[3].rating.count, 1)
        self.assertEquals(job_comments[3].salary, 22)
        self.assertTrue(job_comments[3].crawled)

        self.assertEquals(job_comments[4].comment, datamanager.test_comment_5)
        self.assertEquals(job_comments[4].date, date - relativedelta(months=12))
        self.assertEquals(job_comments[4].rating.rating, float(5) / 5)
        self.assertEquals(job_comments[4].rating.count, 1)
        self.assertEquals(job_comments[4].salary, 20)
        self.assertTrue(job_comments[4].crawled)

        self.assertEquals(job_comments[5].comment, datamanager.test_comment_6)
        self.assertEquals(job_comments[5].date, date - relativedelta(years=3))
        self.assertEquals(job_comments[5].rating.rating, float(2) / 5)
        self.assertEquals(job_comments[5].rating.count, 1)
        self.assertEquals(job_comments[5].salary, 50)
        self.assertTrue(job_comments[5].crawled)

        self.assertEquals(job_comments[6].comment, datamanager.test_comment_7)
        self.assertEquals(job_comments[6].date, date - relativedelta(years=1))
        self.assertEquals(job_comments[6].rating.rating, float(1) / 5)
        self.assertEquals(job_comments[6].rating.count, 1)
        self.assertEquals(job_comments[6].salary, 1)
        self.assertTrue(job_comments[6].crawled)

        self.assertEquals(job_comments[7].comment, '')
        self.assertEquals(job_comments[7].date, date - relativedelta(months=15))
        self.assertEquals(job_comments[7].rating.rating, float(5) / 5)
        self.assertEquals(job_comments[7].rating.count, 1)
        self.assertEquals(job_comments[7].salary, 100)
        self.assertTrue(job_comments[7].crawled)

        employer_comments = self.employer.comments

        self.assertTrue(len(employer_comments) == 0)

        self.employer.comments.delete()


if __name__ == "__main__":
    unittest.main()
