import data.crawler.crawler as crawler
import shared.jobmine as config

import models.term as term

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from itertools import izip_longest
from datetime import datetime


class JobmineCrawler(crawler.Crawler):
    def __init__(self, importer):
        crawler.Crawler.__init__(self, config, importer)

    def login(self):
        self.driver.get(config.url)

        self.logger.info('Loaded {} homepage'.format(config.name))

        self._wait_till_find_element_by(By.ID, 'userid').send_keys(config.username)
        pass_ele = self._wait_till_find_element_by(By.ID, 'pwd')
        pass_ele.send_keys(config.password)
        pass_ele.send_keys(self.keys.ENTER)

    def navigate(self):
        self.wait()

        try:
            job_search_ele_xpath = "(//li[@id='crefli_UW_CO_JOBSRCH_LINK']/a[1])[2]"

            self.logger.info('Loaded menu')

            # Wait for 10 seconds job search element to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, job_search_ele_xpath))
            )

            self.driver.find_element_by_xpath(job_search_ele_xpath).click()

        except TimeoutException:
            self.logger.error('Job search link not found.')
            raise TimeoutException('Job search link not found')

    def crawl(self):
        self.logger.info('Loaded job search page')

        self.set_search_params()

        coop_discipline_menu_1 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP1')
        coop_discipline_menu_2 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP2')
        coop_discipline_menu_3 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP3')

        all_disciplines = coop_discipline_menu_1.find_elements_by_tag_name('option')

        disciplines_len = len(all_disciplines)

        self.logger.info('*' * 10 + ' Beginning crawl ' + '*' * 10)

        # Iterate through all disciplines
        for i, option in enumerate(
                [disciplines[0] for disciplines in izip_longest(*[all_disciplines[1:]] * 3, fillvalue=None)]): #TODO: Fix. Seems to be returning 3 option objects, Could use?

            if i is not 0:
                # Each time we iterate through we click and/or interact with the DOM thus changing it. This
                # means that our old references to elements are stale and need to be reloaded.
                coop_discipline_menu_1 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP1')
                coop_discipline_menu_2 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP2')
                coop_discipline_menu_3 = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP3')

                all_disciplines = coop_discipline_menu_1.find_elements_by_tag_name('option')

                option = all_disciplines[i]

            # Skip empty discipline
            #if not option.get_attribute("value"):
            #    continue

            # Select discipline 1
            option.click()

            self.logger.info('Setting discipline 1: {}'.format(all_disciplines[i].get_attribute("value")))

            # If next discipline exists, set it to discipline 2
            if 0 <= i + 1 < disciplines_len:
                self.logger.info('Setting discipline 2: {}'.format(all_disciplines[i + 1].get_attribute("value")))

                coop_discipline_menu_2.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP2']"
                                                              "/option[@value='41']" # TODO: remove 41 and replace with {}
                                                    .format(all_disciplines[i + 1]
                                                            .get_attribute("value"))).click()
            else:
                coop_discipline_menu_2.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP2']"
                                                              "/option[@value='']").click()
            # If next discipline exists, set it to discipline 3
            if 0 <= i + 2 < disciplines_len:
                self.logger.info('Setting discipline 3: {}'.format(all_disciplines[i + 2].get_attribute("value")))

                coop_discipline_menu_3.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP3']"
                                                              "/option[@value='{}']"
                                                    .format(all_disciplines[i + 2]
                                                            .get_attribute("value"))).click()
            else:
                coop_discipline_menu_3.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP3']"
                                                              "/option[@value='']").click()

            search_ele = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCHDW_UW_CO_DW_SRCHBTN')

            self.logger.info('Initiating search..')

            # Initiate search
            search_ele.click()

            self.wait()

            # Wait for 15 seconds for results to appear
            try:
                WebDriverWait(self.driver, 15).until_not(
                    EC.element_to_be_clickable((By.ID, 'WAIT_win0'))
                )
            except TimeoutException:
                self.logger.error('Job search results did not not load.')
                raise TimeoutException('Job search results did not not load')

            # From 1 to and including total_results
            total_results = int(self.driver.find_element_by_class_name('PSGRIDCOUNTER').text.split()[2])

            self.logger.info('{} results found'.format(total_results))

            # Iterate through all jobs in current page
            for index in range(0, total_results - 1):
                employer_name = self._wait_till_find_element_by \
                    (By.ID, 'UW_CO_JOBRES_VW_UW_CO_PARENT_NAME${}'.format(index)).text

                job_title = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBTITLE_HL${}'.format(index)).text

                self.logger.info('Importing job: {} from {}'.format(job_title, employer_name))

                location = self._wait_till_find_element_by \
                    (By.ID, 'UW_CO_JOBRES_VW_UW_CO_WORK_LOCATN${}'.format(index)).text

                openings = self._wait_till_find_element_by \
                    (By.ID, 'UW_CO_JOBRES_VW_UW_CO_OPENGS${}'.format(index)).text

                applicants = self._wait_till_find_element_by \
                    (By.ID, 'UW_CO_JOBAPP_CT_UW_CO_MAX_RESUMES${}'.format(index)).text

                self.driver.execute_script("javascript:submitAction_win0(document.win0,'UW_CO_JOBTITLE_HL${}');"
                                           .format(index))

                self.wait()

                # Wait for new window to open containing job information
                WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)

                # Switch to new window
                self.driver.switch_to.window(self.driver.window_handles[1])

                self._switch_to_iframe('ptifrmtgtframe')

                summary = self._wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_VW_UW_CO_JOB_DESCR').text

                self.driver.close()

                # Wait for job window to close
                WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 1)

                # Switch back to job search page
                self.driver.switch_to.window(self.driver.window_handles[0])

                self._switch_to_iframe('ptifrmtgtframe')

                now = datetime.now()

                self.importer.import_job(employer_name=employer_name, job_title=job_title,
                                         term=term.get_term(now.month), location=location, openings=openings,
                                         applicants=applicants, summary=summary, date=now)

                break

            break

    def set_search_params(self):
        try:
            self.logger.info('Setting job search parameters')

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
                if option.text == 'Approved': # TODO: change to Posted
                    option.click()
                    break

            now = datetime.now()

            coop_term = term.get_coop_term(now)

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


if __name__ == '__main__':
    jobmine_crawler = JobmineCrawler(None)
    jobmine_crawler.run()
