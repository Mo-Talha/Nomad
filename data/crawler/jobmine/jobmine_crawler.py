from itertools import izip_longest
from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import data.analysis.importer as importer
import data.crawler.crawler as crawler

import shared.jobmine as config

from models.job import Job
import models.term as Term


class JobmineCrawler(crawler.Crawler):
    def __init__(self):
        crawler.Crawler.__init__(self, config)

    def login(self):
        self.driver.get(config.url)

        self.logger.info(self.config.name, 'Loaded {} homepage'.format(config.name))

        self._wait_till_find_element_by(By.ID, 'userid').send_keys(config.username)

        pass_ele = self._wait_till_find_element_by(By.ID, 'pwd')
        pass_ele.send_keys(config.password)
        pass_ele.send_keys(Keys.ENTER)

    def navigate(self):
        self.wait()

        try:
            job_search_ele_xpath = "(//li[@id='crefli_UW_CO_JOBSRCH_LINK']/a[1])[2]"

            self.logger.info(self.config.name, 'Loaded menu')

            # Wait for 10 seconds job search element to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, job_search_ele_xpath))
            )

            self.driver.find_element_by_xpath(job_search_ele_xpath).click()

        except TimeoutException:
            self.logger.error('Job search link not found.')
            raise TimeoutException('Job search link not found')

    def crawl(self):
        self.logger.info(self.config.name, 'Loaded job search page')

        self._set_search_params()

        coop_discipline_menu_1 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP1')
        coop_discipline_menu_2 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP2')
        coop_discipline_menu_3 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP3')

        all_disciplines = coop_discipline_menu_1.find_elements_by_tag_name('option')[1:]

        disciplines_len = len(all_disciplines)

        self.logger.info(self.config.name, '*' * 10 + ' Beginning crawl ' + '*' * 10)

        discipline_index = 0

        for option in [disciplines[0] for disciplines in izip_longest(*[iter(all_disciplines)] * 3)]:

            # Each time we iterate through we click and/or interact with the DOM thus changing it. This
            # means that our old references to elements are stale and need to be reloaded
            coop_discipline_menu_1 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP1')
            coop_discipline_menu_2 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP2')
            coop_discipline_menu_3 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP3')

            all_disciplines = coop_discipline_menu_1.find_elements_by_tag_name('option')[1:]

            self.logger.info(self.config.name, 'Setting discipline 1: {}'
                             .format(all_disciplines[discipline_index].text))

            # Select discipline 1
            all_disciplines[discipline_index].click()

            # If next discipline exists, set it to discipline 2
            if 0 <= discipline_index + 1 < disciplines_len:
                self.logger.info(self.config.name, 'Setting discipline 2: {}'
                                 .format(all_disciplines[discipline_index + 1].text))

                coop_discipline_menu_2.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP2']"
                                                              "/option[@value='{}']"
                                                    .format(all_disciplines[discipline_index + 1]
                                                            .get_attribute("value"))).click()
            else:
                coop_discipline_menu_2.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP2']"
                                                              "/option[@value='']").click()

            # If next discipline exists, set it to discipline 3
            if 0 <= discipline_index + 2 < disciplines_len:
                self.logger.info(self.config.name, 'Setting discipline 3: {}'
                                 .format(all_disciplines[discipline_index + 2].text))

                coop_discipline_menu_3.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP3']"
                                                              "/option[@value='{}']"
                                                    .format(all_disciplines[discipline_index + 2]
                                                            .get_attribute("value"))).click()
            else:
                coop_discipline_menu_3.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP3']"
                                                              "/option[@value='']").click()

            discipline_index += 3

            search_ele = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCHDW_UW_CO_DW_SRCHBTN')

            self.logger.info(self.config.name, 'Initiating search..')

            # Initiate search
            search_ele.click()

            self.wait()

            self._wait_for_job_results()

            # From 1 to and including total_results
            total_results = int(self.driver.find_element_by_class_name('PSGRIDCOUNTER').text.split()[2])

            self.logger.info(self.config.name, '{} results found'.format(total_results))

            # Jobmine job index is from 0-24 for each page assuming view is 25 per page
            job_index = 0

            for index in range(0, total_results):

                # For some reason when there are no jobs posted, jobmine says 1 total results
                if total_results <= 1:
                    continue

                employer_name = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBRES_VW_UW_CO_PARENT_NAME${}'
                                                                .format(job_index)).text

                job_title = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBTITLE_HL${}'.format(job_index)).text

                location = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBRES_VW_UW_CO_WORK_LOCATN${}'
                                                           .format(job_index)).text

                openings = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBRES_VW_UW_CO_OPENGS${}'
                                                           .format(job_index)).text

                applicants = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBAPP_CT_UW_CO_MAX_RESUMES${}'
                                                             .format(job_index)).text

                # Redis job key for jobmine crawler
                job_key = 'jobmine.{}.{}'.format(employer_name, job_title).replace(' ', '.')

                if not self.redis.exists(job_key):
                    self.driver.execute_script("javascript:submitAction_win0(document.win0,'UW_CO_JOBTITLE_HL${}');"
                                               .format(job_index))

                    # Wait for new job window to open
                    WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) == 2)

                    # Switch to new window
                    self.driver.switch_to.window(self.driver.window_handles[1])

                    self._switch_to_iframe('ptifrmtgtframe')

                    summary = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_VW_UW_CO_JOB_DESCR').text

                    programs = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR')\
                        .text.strip(',')
                    programs_2 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR100')\
                        .text.strip(',')

                    # If 2nd programs line exists
                    if not programs_2.isspace():
                        programs += ',' + programs_2

                    job_levels = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR_100').text

                    job_url = self.driver.current_url

                    self.driver.close()

                    # Wait for job window to close
                    WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) == 1)

                    # Switch back to job search page
                    self.driver.switch_to.window(self.driver.window_handles[0])

                    self._switch_to_iframe('ptifrmtgtframe')

                    now = datetime.now()

                    importer.import_job(employer_name=employer_name, job_title=job_title,
                                        term=Term.get_term(now.month), location=location, levels=job_levels,
                                        openings=openings, applicants=applicants, summary=summary, date=now,
                                        programs=programs, url=job_url)

                    self.redis.set(job_key, 1)
                    self.redis.expire(job_key, self.config.cache_interval)

                    self.wait()

                else:
                    self.logger.info(self.config.name, 'Job: {} from {} already exists in cache, skipping..'
                                     .format(job_title, employer_name))

                if 0 <= job_index < 24:
                    job_index += 1

                else:
                    self.logger.info(self.config.name, 'Traversing to next page..')

                    job_index = 0

                    next_page = self._wait_till_find_element_by(By.NAME, 'UW_CO_JOBRES_VW$hdown$img$0')
                    next_page.click()

                    self._wait_for_job_results()

        self.logger.info(self.config.name, '*** Done importing new jobs ***')

        self.logger.info(self.config.name, '*** Updating active jobs ***')

        # Iterate through "active" jobs in DB (i.e. non-deprecated, current term)
        for job_url in Job.get_active_job_urls():
            self.driver.get(job_url)

            employer_name = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_EMPUNITDIV').text

            job_title = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_VW_UW_CO_JOB_TITLE').text

            job_key = 'jobmine.{}.{}'.format(employer_name, job_title).replace(' ', '.')

            if not self.redis.exists(job_key):
                location = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_VW_UW_CO_WORK_LOCATN').text

                openings = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_VW_UW_CO_AVAIL_OPENGS').text

                summary = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_VW_UW_CO_JOB_DESCR').text

                programs = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR').text.strip(',')
                programs_2 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR100').text.strip(',')

                if not programs_2.isspace():
                    programs += ',' + programs_2

                levels = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR_100').text

                now = datetime.now()

                importer.import_job(employer_name=employer_name, job_title=job_title,
                                    term=Term.get_term(now.month), location=location, levels=levels,
                                    openings=openings, summary=summary, date=now,
                                    programs=programs, applicants=-1)

                self.wait()

            else:
                self.logger.info(self.config.name, 'Job: {} from {} already exists in cache, skipping..'
                                 .format(job_title, employer_name))

    def _set_search_params(self):
        try:
            self.logger.info(self.config.name, 'Setting job search parameters')

            self._switch_to_iframe('ptifrmtgtframe')

            self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_JR')

        except TimeoutException:
            self.logger.error('Job search page did not not load.')
            raise TimeoutException('Job search page did not not load')

        else:
            coop_junior_ele = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_JR')
            coop_interm_ele = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_INT')
            coop_senior_ele = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_SR')
            coop_type_ele = self._wait_till_find_element_by(By.ID, 'TYPE_COOP')

            if not coop_junior_ele.is_selected():
                coop_junior_ele.click()

            if not coop_interm_ele.is_selected():
                coop_interm_ele.click()

            if not coop_senior_ele.is_selected():
                coop_senior_ele.click()

            if not coop_type_ele.is_selected():
                coop_type_ele.click()

            coop_job_status_ele = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_JS_JOBSTATUS')

            for option in coop_job_status_ele.find_elements_by_tag_name('option'):
                if option.text == 'Posted':
                    option.click()
                    break

            now = datetime.now()

            coop_term = Term.get_coop_term(now)

            # Get next term since each term is looking for a co-op position for next term
            if 1 <= now.month <= 4:
                coop_term += 4
            elif 5 <= now.month <= 8:
                coop_term += 4
            elif 9 <= now.month <= 12:
                coop_term += 2

            coop_term_ele = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_WT_SESSION')
            coop_term_ele.clear()

            coop_term_ele.send_keys(coop_term)

    def _wait_for_job_results(self, wait=15):
        # Wait for 15 seconds for results to appear
        try:
            WebDriverWait(self.driver, wait).until_not(
                EC.element_to_be_clickable((By.ID, 'WAIT_win0'))
            )
        except TimeoutException:
            self.logger.error('Job search results did not not load.')
            raise TimeoutException('Job search results did not not load')
