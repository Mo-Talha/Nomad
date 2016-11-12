import unittest
import time
import mongoengine
import redis

from datetime import datetime

import data.analysis.importer as importer
import tests.analysis.importer_datamanager as datamanager

from models.exceptions import DataIntegrityError
from models.employer import Employer
from models.job import Job
import models.term as Term

import shared.secrets as secrets


redis = redis.StrictRedis(host=secrets.REDIS_HOST, port=secrets.REDIS_PORT, db=secrets.REDIS_DB)
mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)


class JobmineImporterTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_normal_import(self):
        employer_name = 'Test Employer 1'
        job_title = 'Test Job Title 1'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Toronto'
        job_levels = ['Junior', 'Intermediate', 'Senior']
        openings = 10
        applicants = 50
        summary = datamanager.test_summary
        programs = ['MATH-Computer Science', 'ENG-Computer', 'ENG-Civil']
        job_url = 'https://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job.title, job_title)
        self.assertEqual(job.url, job_url)
        self.assertEqual(job.term, term)
        self.assertEqual(job.location[0].name, location)
        self.assertTrue(int(round(job.location[0].longitude)) == -79)
        self.assertTrue(int(round(job.location[0].latitude)) == 44)
        self.assertEqual(job.openings, openings)
        self.assertEqual(job.remaining, openings)
        self.assertEqual(job.hire_rate.rating, 0.0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), set(job_levels))
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), set(programs))
        self.assertFalse(job.deprecated)

        job.delete()
        employer.delete()

        time.sleep(2)

    def test_normal_unicode_import(self):
        employer_name = u'Test Employer 2'
        job_title = u'Test Job Title 2'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = u'Toronto'
        job_levels = [u'Junior', u'Intermediate', u'Senior']
        openings = 10
        applicants = 50
        summary = datamanager.test_summary_unicode
        programs = [u'MATH-Computer Science', u'ENG-Computer', u'ENG-Civil']
        job_url = u'https://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job.title, job_title)
        self.assertEqual(job.url, job_url)
        self.assertEqual(job.term, term)
        self.assertEqual(job.location[0].name, location)
        self.assertTrue(int(round(job.location[0].longitude)) == -79)
        self.assertTrue(int(round(job.location[0].latitude)) == 44)
        self.assertEqual(job.openings, openings)
        self.assertEqual(job.remaining, openings)
        self.assertEqual(job.hire_rate.rating, 0.0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), set(job_levels))
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), set(programs))
        self.assertFalse(job.deprecated)

        job.delete()
        employer.delete()

        time.sleep(2)

    def test_edge_cases_import(self):
        employer_name = '123 Test Employer 3'
        job_title = '123 Test Job Title 3'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'burlington'
        job_levels = ['junior', 'intermediate', 'Senior']
        openings = 1
        applicants = 0
        summary = ''
        programs = ['math computer science', 'eng computer', 'eng  - Civil', 'ayy lmao']
        job_url = 'https://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job.title, job_title)
        self.assertEqual(job.url, job_url)
        self.assertEqual(job.term, term)
        self.assertEqual(job.location[0].name, location)
        self.assertTrue(int(round(job.location[0].longitude)) == -80)
        self.assertTrue(int(round(job.location[0].latitude)) == 43)
        self.assertEqual(job.openings, openings)
        self.assertEqual(job.remaining, openings)
        self.assertEqual(job.hire_rate.rating, 0.0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), {'Junior', 'Intermediate', 'Senior'})
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), {'MATH-Computer Science', 'ENG-Computer', 'ENG-Civil'})
        self.assertFalse(job.deprecated)

        job.delete()
        employer.delete()

        time.sleep(2)

    def test_edge_cases_unicode_import(self):
        employer_name = u'123 Test Employer 4'
        job_title = u'123 Test Job Title 4'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = u'burlington'
        job_levels = [u'junior', u'intermediate', u'Senior']
        openings = 1
        applicants = 0
        summary = u''
        programs = [u'math computer science', u'eng computer', u'eng  - Civil', u'ayy lmao']
        job_url = u'https://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job.title, job_title)
        self.assertEqual(job.url, job_url)
        self.assertEqual(job.term, term)
        self.assertEqual(job.location[0].name, location)
        self.assertTrue(int(round(job.location[0].longitude)) == -80)
        self.assertTrue(int(round(job.location[0].latitude)) == 43)
        self.assertEqual(job.openings, openings)
        self.assertEqual(job.remaining, openings)
        self.assertEqual(job.hire_rate.rating, 0.0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), {u'Junior', u'Intermediate', u'Senior'})
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), {u'MATH-Computer Science', u'ENG-Computer', u'ENG-Civil'})
        self.assertFalse(job.deprecated)

        job.delete()
        employer.delete()

        time.sleep(2)

    def test_employer_exists_job_does_not_exist_import(self):
        employer_name = 'Test Employer 5'
        job_title = 'Test Job Title 5'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Toronto'
        job_levels = ['Junior', 'Intermediate']
        openings = 4
        applicants = 23
        summary = datamanager.test_summary_medium
        programs = ['ENG-Electrical', 'ENG-Computer', 'SCI-Psychology', 'MATH-Business Administration']
        job_url = 'https://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job_1 = Job.objects(id__in=[job_1.id for job_1 in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job_1.title, job_title)
        self.assertEqual(job_1.url, job_url)
        self.assertEqual(job_1.term, term)
        self.assertEqual(job_1.location[0].name, location)
        self.assertTrue(int(round(job_1.location[0].longitude)) == -79)
        self.assertTrue(int(round(job_1.location[0].latitude)) == 44)
        self.assertEqual(job_1.openings, openings)
        self.assertEqual(job_1.remaining, openings)
        self.assertEqual(job_1.hire_rate.rating, 0.0)
        self.assertEqual(job_1.applicants[0].applicants, applicants)
        self.assertEqual(job_1.applicants[0].date.year, now.year)
        self.assertEqual(job_1.applicants[0].date.month, now.month)
        self.assertEqual(job_1.applicants[0].date.day, now.day)
        self.assertEqual(set(job_1.levels), set(job_levels))
        self.assertTrue(len(job_1.comments) == 0)
        self.assertEqual(set(job_1.programs), set(programs))
        self.assertFalse(job_1.deprecated)

        job_title = 'Test Job Title 6'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Toronto'
        job_levels = ['Junior', 'Intermediate']
        openings = 7
        applicants = 73
        summary = datamanager.test_summary_small
        programs = ['ENG-Electrical', 'ENG-Computer', 'ENV-Planning', 'MATH-Business Administration']
        job_url = 'https://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job_2 = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job_2.title, job_title)
        self.assertEqual(job_2.url, job_url)
        self.assertEqual(job_2.term, term)
        self.assertEqual(job_2.location[0].name, location)
        self.assertTrue(int(round(job_2.location[0].longitude)) == -79)
        self.assertTrue(int(round(job_2.location[0].latitude)) == 44)
        self.assertEqual(job_2.openings, openings)
        self.assertEqual(job_2.remaining, openings)
        self.assertEqual(job_2.hire_rate.rating, 0.0)
        self.assertEqual(job_2.applicants[0].applicants, applicants)
        self.assertEqual(job_2.applicants[0].date.year, now.year)
        self.assertEqual(job_2.applicants[0].date.month, now.month)
        self.assertEqual(job_2.applicants[0].date.day, now.day)
        self.assertEqual(set(job_2.levels), set(job_levels))
        self.assertTrue(len(job_2.comments) == 0)
        self.assertEqual(set(job_2.programs), set(programs))
        self.assertFalse(job_2.deprecated)

        job_1.delete()
        job_2.delete()
        employer.delete()

        time.sleep(2)

    def test_employer_exists_job_exist_update_invalid_year_import(self):
        employer_name = 'Test Employer 7'
        job_title = 'Test Job Title 7'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Waterloo'
        job_levels = ['Junior']
        openings = 4
        applicants = 10
        summary = datamanager.test_summary_medium
        programs = ['ENG-Electrical', 'ENG-Computer', 'SCI-Psychology', 'MATH-Business Administration']
        job_url = 'https://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job.title, job_title)
        self.assertEqual(job.url, job_url)
        self.assertEqual(job.term, term)
        self.assertEqual(job.location[0].name, location)
        self.assertTrue(int(round(job.location[0].longitude)) == -81)
        self.assertTrue(int(round(job.location[0].latitude)) == 43)
        self.assertEqual(job.openings, openings)
        self.assertEqual(job.remaining, openings)
        self.assertEqual(job.hire_rate.rating, 0.0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), set(job_levels))
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), set(programs))
        self.assertFalse(job.deprecated)

        now = datetime(2010, 1, 1)

        self.assertRaises(DataIntegrityError, importer.import_job, employer_name=employer_name, job_title=job_title,
                          term=term, location=location, levels=job_levels, openings=openings, applicants=applicants,
                          summary=summary, date=now, programs=programs, url=job_url)
        job.delete()
        employer.delete()

        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
