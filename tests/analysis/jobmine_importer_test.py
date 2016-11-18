import unittest
import mongoengine
import redis

from mongoengine import connection
from datetime import datetime
from bson.objectid import ObjectId

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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(job.hire_rate.count, 0)
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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(job.hire_rate.count, 0)
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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(job.hire_rate.count, 0)
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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(job.hire_rate.count, 0)
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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(job.hire_rate.count, 0)
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

    def test_employer_exists_job_exist_update_summary_1_import(self):
        employer_name = 'Test Employer 8'
        job_title = 'Test Job Title 8'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Waterloo'
        job_levels = ['Senior']
        openings = 455
        applicants = 150
        summary = datamanager.test_summary_small_unicode
        programs = ['ENG-Electrical']
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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(job.hire_rate.count, 0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), set(job_levels))
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), set(programs))
        self.assertFalse(job.deprecated)

        summary = datamanager.test_summary_small_unicode + u" appending random stuff so its deprecated"

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer.reload()
        job.reload()

        self.assertTrue(job.deprecated)

        old_job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title, deprecated=True).first()
        old_job.delete()

        job_2 = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title, deprecated=False).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertEqual(employer.overall.count, 0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job_2.title, job_title)
        self.assertEqual(job_2.url, job_url)
        self.assertEqual(job_2.term, term)
        self.assertEqual(job_2.location[0].name, location)
        self.assertTrue(int(round(job_2.location[0].longitude)) == -81)
        self.assertTrue(int(round(job_2.location[0].latitude)) == 43)
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

        job_2.delete()
        employer.delete()

    def test_employer_exists_job_exist_update_summary_2_import(self):
        employer_name = 'Test Employer 9'
        job_title = 'Test Job Title 9'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Waterloo'
        job_levels = ['Senior']
        openings = 455
        applicants = 150
        summary = datamanager.test_summary_small_unicode
        programs = ['ENG-Electrical']
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
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(job.hire_rate.count, 0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), set(job_levels))
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), set(programs))
        self.assertFalse(job.deprecated)

        summary = datamanager.test_summary_small + "             "

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, applicants=applicants,
                            summary=summary, date=now, programs=programs, url=job_url)

        employer.reload()
        job.reload()

        self.assertFalse(job.deprecated)

        job_2 = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title, deprecated=True).first()

        self.assertEquals(job_2, None)

        job.delete()
        employer.delete()

    def test_employer_exists_job_exist_update_job_new_term_import(self):
        employer_name = 'Test Employer 10'
        job_title = 'Test Job Title 10'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Waterloo'
        job_levels = ['Intermediate']
        openings = 10
        remaining = 5
        applicants = 1
        summary = datamanager.test_summary_small
        programs = ['ENG-Computer']
        job_url = 'http://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings, remaining=remaining,
                            applicants=applicants, summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertEqual(employer.overall.count, 0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job.title, job_title)
        self.assertEqual(job.url, job_url)
        self.assertEqual(job.term, term)
        self.assertEqual(job.location[0].name, location)
        self.assertTrue(int(round(job.location[0].longitude)) == -81)
        self.assertTrue(int(round(job.location[0].latitude)) == 43)
        self.assertEqual(job.openings, openings)
        self.assertEqual(job.remaining, remaining)
        self.assertEqual(job.hire_rate.rating, 0.0)
        self.assertEqual(job.hire_rate.count, 0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), set(job_levels))
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), set(programs))
        self.assertFalse(job.deprecated)

        now_update = datetime(datetime.now().year + 1, 1, 1)
        term_update = Term.get_term(now_update.month)
        location_update = 'Toronto'
        job_levels_update = ['Intermediate']
        openings_update = 10
        remaining_update = 5
        applicants_update = 5
        summary_update = datamanager.test_summary_small
        programs_update = ['ENG-Civil']
        job_url_update = 'http://testurl.com/new'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term_update,
                            location=location_update, levels=job_levels_update, openings=openings_update,
                            remaining=remaining_update, applicants=applicants_update, summary=summary_update,
                            date=now_update, programs=programs_update, url=job_url_update)

        location_update = location_update.lower()

        employer.reload()
        job.reload()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertEqual(employer.overall.count, 0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job.title, job_title)
        self.assertEqual(job.url, job_url_update)
        self.assertEqual(job.term, term_update)
        self.assertEqual(job.location[0].name, location)
        self.assertEqual(job.location[1].name, location_update)
        self.assertTrue(int(round(job.location[0].longitude)) == -81)
        self.assertTrue(int(round(job.location[0].latitude)) == 43)
        self.assertTrue(int(round(job.location[1].longitude)) == -79)
        self.assertTrue(int(round(job.location[1].latitude)) == 44)
        self.assertEqual(job.openings, openings_update)
        self.assertEqual(job.remaining, remaining_update)
        self.assertEqual(job.hire_rate.rating, 0.5)
        self.assertEqual(job.hire_rate.count, 1)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(job.applicants[1].applicants, applicants_update)
        self.assertEqual(job.applicants[1].date.year, now_update.year)
        self.assertEqual(job.applicants[1].date.month, now_update.month)
        self.assertEqual(job.applicants[1].date.day, now_update.day)
        self.assertEqual(set(job.levels), set(job_levels_update))
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), set(programs_update))
        self.assertFalse(job.deprecated)

        job_2 = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title, deprecated=True).first()

        self.assertEquals(job_2, None)

        job.delete()
        employer.delete()

    def test_employer_exists_job_exist_update_current_term_import(self):
        employer_name = 'Test Employer 11'
        job_title = 'Test Job Title 11'
        now = datetime.now()
        term = Term.get_term(now.month)
        location = 'Waterloo'
        job_levels = ['Senior']
        openings = 10
        applicants = 1
        summary = datamanager.test_summary_small
        programs = ['ARCH-Architecture']
        job_url = 'http://testurl.com'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location, levels=job_levels, openings=openings,
                            applicants=applicants, summary=summary, date=now, programs=programs, url=job_url)

        employer_name = employer_name.lower()
        job_title = job_title.lower()
        location = location.lower()

        employer = Employer.objects(name=employer_name).no_dereference().first()

        job = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title).first()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertEqual(employer.overall.count, 0)
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
        self.assertEqual(job.hire_rate.count, 0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(set(job.levels), set(job_levels))
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), set(programs))
        self.assertFalse(job.deprecated)

        location_update = 'Toronto'
        job_levels_update = ['Intermediate']
        openings_update = 5
        applicants_update = 5
        summary_update = datamanager.test_summary_small
        programs_update = ['ENG-Civil']
        job_url_update = 'http://testurl.com/new'

        importer.import_job(employer_name=employer_name, job_title=job_title, term=term,
                            location=location_update, levels=job_levels_update, openings=openings_update,
                            applicants=applicants_update, summary=summary_update,
                            date=now, programs=programs_update, url=job_url_update)

        location_update = location_update.lower()

        employer.reload()
        job.reload()

        self.assertEqual(employer.name, employer_name)
        self.assertEqual(employer.overall.rating, 0.0)
        self.assertEqual(employer.overall.count, 0)
        self.assertTrue(len(employer.warnings) == 0)
        self.assertTrue(len(employer.comments) == 0)

        self.assertEqual(job.title, job_title)
        self.assertEqual(job.url, job_url_update)
        self.assertEqual(job.term, term)
        self.assertEqual(job.location[0].name, location)
        self.assertEqual(job.location[1].name, location_update)
        self.assertTrue(int(round(job.location[0].longitude)) == -81)
        self.assertTrue(int(round(job.location[0].latitude)) == 43)
        self.assertTrue(int(round(job.location[1].longitude)) == -79)
        self.assertTrue(int(round(job.location[1].latitude)) == 44)
        self.assertEqual(job.openings, openings)
        self.assertEqual(job.remaining, openings_update)
        self.assertEqual(job.hire_rate.rating, 0.0)
        self.assertEqual(job.hire_rate.count, 0)
        self.assertEqual(job.applicants[0].applicants, applicants)
        self.assertEqual(job.applicants[0].date.year, now.year)
        self.assertEqual(job.applicants[0].date.month, now.month)
        self.assertEqual(job.applicants[0].date.day, now.day)
        self.assertEqual(job.applicants[1].applicants, applicants_update)
        self.assertEqual(job.applicants[1].date.year, now.year)
        self.assertEqual(job.applicants[1].date.month, now.month)
        self.assertEqual(job.applicants[1].date.day, now.day)
        self.assertEqual(set(job.levels), {'Intermediate', 'Senior'})
        self.assertTrue(len(job.comments) == 0)
        self.assertEqual(set(job.programs), {'ARCH-Architecture', 'ENG-Civil'})
        self.assertFalse(job.deprecated)

        job_2 = Job.objects(id__in=[job.id for job in employer.jobs], title=job_title, deprecated=True).first()

        self.assertEquals(job_2, None)

        job.delete()
        employer.delete()

if __name__ == "__main__":
    unittest.main()
