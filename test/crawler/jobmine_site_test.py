import time
import unittest

from itertools import izip_longest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import models.term as Term

import shared.jobmine as config


class JobmineSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS(service_args=['--web-security=no', '--webdriver-loglevel=NONE'])
        self.driver.get(config.url)

        user_ele = self.wait_till_find_element_by(By.ID, 'userid')
        self.assertEquals(user_ele.tag_name, u'input')

        user_ele.send_keys(config.username)

        pass_ele = self.wait_till_find_element_by(By.ID, 'pwd')
        self.assertEquals(pass_ele.tag_name, u'input')

        pass_ele.send_keys(config.password)
        pass_ele.send_keys(Keys.ENTER)

        self.wait()

    def tearDown(self):
        self.driver.close()

    def test_elements_exists(self):
        job_inquiry_ele = self.wait_till_find_element_by(By.XPATH, "(//li[@id='crefli_UW_CO_JOBSRCH_LINK']//a[1])[2]")

        self.assertEquals(job_inquiry_ele.tag_name, u'a')
        self.assertIn(u'Job Inquiry', job_inquiry_ele.text)

        job_inquiry_ele.click()

        self.wait()

        iframe = self.wait_till_find_element_by(By.ID, 'ptifrmtgtframe')
        self.assertEquals(iframe.tag_name, u'iframe')

        self.switch_to_iframe_by_id(u'ptifrmtgtframe')

        coop_junior_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_JR')
        self.assertEquals(coop_junior_ele.tag_name, u'input')

        coop_junior_ele_label = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_JR_LBL')
        self.assertIn(u'Junior', coop_junior_ele_label.text)

        coop_interm_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_INT')
        self.assertEquals(coop_interm_ele.tag_name, u'input')

        coop_interm_ele_label = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_INT_LBL')
        self.assertIn(u'Intermediate', coop_interm_ele_label.text)

        coop_senior_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_SR')
        self.assertEquals(coop_senior_ele.tag_name, u'input')

        coop_senior_ele_label = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_SR_LBL')
        self.assertIn(u'Senior', coop_senior_ele_label.text)

        coop_type_ele = self.wait_till_find_element_by(By.ID, 'TYPE_COOP')
        self.assertEquals(coop_type_ele.tag_name, u'input')

        coop_type_ele_label = self.wait_till_find_element_by(By.ID, 'TYPE_COOP_LBL')
        self.assertIn(u'Co-op', coop_type_ele_label.text)

        if not coop_junior_ele.is_selected():
            coop_junior_ele.click()

        if not coop_interm_ele.is_selected():
            coop_interm_ele.click()

        if not coop_senior_ele.is_selected():
            coop_senior_ele.click()

        if not coop_type_ele.is_selected():
            coop_type_ele.click()

        coop_job_status_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_JS_JOBSTATUS')
        self.assertEquals(coop_job_status_ele.tag_name, u'select')

        for option in coop_job_status_ele.find_elements_by_tag_name('option'):
            if option.text == 'Posted':
                option.click()
                break
        else:
            self.assertTrue(False, 'Posted option not found in element: UW_CO_JOBSRCH_UW_CO_JS_JOBSTATUS')

        now = datetime.now()

        coop_term = Term.get_coop_term(now)

        # Get next term since each term is looking for a co-op position for next term
        if 1 <= now.month <= 4:
            coop_term += 4
        elif 5 <= now.month <= 8:
            coop_term += 4
        elif 9 <= now.month <= 12:
            coop_term += 2

        coop_term_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_WT_SESSION')
        self.assertEquals(coop_term_ele.tag_name, u'input')
        coop_term_ele.clear()
        coop_term_ele.send_keys(coop_term)

        employer_name_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_EMPLYR_NAME')
        self.assertEquals(employer_name_ele.tag_name, u'input')
        employer_name_ele.clear()

        job_title_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_JOB_TITLE')
        self.assertEquals(job_title_ele.tag_name, u'input')
        job_title_ele.clear()

        location_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_LOCATION')
        self.assertEquals(location_ele.tag_name, u'input')
        location_ele.clear()

        search_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCHDW_UW_CO_DW_SRCHBTN')
        self.assertEquals(search_ele.tag_name, u'input')
        self.assertIn(u'Search', search_ele.get_attribute('value'))

        coop_discipline_menu_1 = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP1')
        self.assertEquals(coop_discipline_menu_1.tag_name, u'select')

        coop_discipline_menu_2 = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP2')
        self.assertEquals(coop_discipline_menu_2.tag_name, u'select')

        coop_discipline_menu_3 = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP3')
        self.assertEquals(coop_discipline_menu_3.tag_name, u'select')

        # First option should be blank
        self.assertFalse(coop_discipline_menu_1.find_elements_by_tag_name('option')[0].text.strip())
        self.assertFalse(coop_discipline_menu_2.find_elements_by_tag_name('option')[0].text.strip())
        self.assertFalse(coop_discipline_menu_3.find_elements_by_tag_name('option')[0].text.strip())

        all_disciplines = coop_discipline_menu_1.find_elements_by_tag_name('option')[1:]

        disciplines_len = len(all_disciplines)
        discipline_index = 0

        for option in [disciplines[0] for disciplines in izip_longest(*[iter(all_disciplines)] * 3)]:

            # Each time we iterate through we click and/or interact with the DOM thus changing it. This
            # means that our old references to elements are stale and need to be reloaded
            coop_discipline_menu_1 = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP1')
            coop_discipline_menu_2 = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP2')
            coop_discipline_menu_3 = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCH_UW_CO_ADV_DISCP3')

            all_disciplines = coop_discipline_menu_1.find_elements_by_tag_name('option')[1:]

            all_disciplines[discipline_index].click()

            for discipline in all_disciplines:
                if discipline.text.strip() == 'MATH-Computer Science':
                    discipline.click()
                    break

            # If next discipline exists, set it to discipline 2
            if 0 <= discipline_index + 1 < disciplines_len:
                coop_discipline_menu_2.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP2']"
                                                              "/option[@value='{}']"
                                                    .format(all_disciplines[discipline_index + 1]
                                                            .get_attribute("value"))).click()
            else:
                coop_discipline_menu_2.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP2']"
                                                              "/option[@value='']").click()

            # If next discipline exists, set it to discipline 3
            if 0 <= discipline_index + 2 < disciplines_len:
                coop_discipline_menu_3.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP3']"
                                                              "/option[@value='{}']"
                                                    .format(all_disciplines[discipline_index + 2]
                                                            .get_attribute("value"))).click()
            else:
                coop_discipline_menu_3.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP3']"
                                                              "/option[@value='']").click()

            discipline_index += 3

            search_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBSRCHDW_UW_CO_DW_SRCHBTN')

            # Initiate search
            search_ele.click()

            self.wait()

            self._wait_for_job_results()

            counter_ele = self.driver.find_element_by_class_name('PSGRIDCOUNTER')
            self.assertEquals(counter_ele.tag_name, u'span')

            # From 1 to and including total_results
            total_results = int(counter_ele.text.split()[2])

            if total_results >= 2:
                self.wait_till_find_element_by(By.ID, 'UW_CO_JOBRES_VW_UW_CO_PARENT_NAME$0')
                self.wait_till_find_element_by(By.ID, 'UW_CO_JOBTITLE_HL$0')
                self.wait_till_find_element_by(By.ID, 'UW_CO_JOBRES_VW_UW_CO_WORK_LOCATN$0')
                self.wait_till_find_element_by(By.ID, 'UW_CO_JOBRES_VW_UW_CO_OPENGS$0')
                self.wait_till_find_element_by(By.ID, 'UW_CO_JOBAPP_CT_UW_CO_MAX_RESUMES$0')

                self.driver.execute_script("javascript:submitAction_win0(document.win0,'UW_CO_JOBTITLE_HL$0');")

                # Wait for new job window to open
                WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) == 2)

                # Switch to new window
                self.driver.switch_to.window(self.driver.window_handles[1])

                iframe = self.wait_till_find_element_by(By.ID, 'ptifrmtgtframe')
                self.assertEquals(iframe.tag_name, u'iframe')

                self.switch_to_iframe_by_id(u'ptifrmtgtframe')

                summary_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_VW_UW_CO_JOB_DESCR')
                self.assertEquals(summary_ele.tag_name, u'span')

                programs_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR')
                self.assertEquals(programs_ele.tag_name, u'span')

                programs_2_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR100')
                self.assertEquals(programs_2_ele.tag_name, u'span')

                job_levels_ele = self.wait_till_find_element_by(By.ID, 'UW_CO_JOBDTL_DW_UW_CO_DESCR_100')
                self.assertEquals(job_levels_ele.tag_name, u'span')

                break

    @staticmethod
    def wait():
        time.sleep(config.crawler_interval)

    def wait_till_find_element_by(self, by, element_id, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((by, element_id))
            )

            return self.driver.find_element(by, element_id)
        except TimeoutException:
            raise TimeoutException('Could not find element: ' + element_id)

    def switch_to_iframe_by_id(self, iframe_id, wait=10):
        try:
            # Wait for iFrame to load (Sometimes an issue in PhantomJS)
            WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((By.ID, iframe_id))
            )

            self.driver.switch_to.frame(self.driver.find_element_by_id(iframe_id))
        except TimeoutException:
            raise TimeoutException('Could not find iFrame: ' + iframe_id)

    def _wait_for_job_results(self, wait=15):
        # Wait for 15 seconds for results to appear
        try:
            WebDriverWait(self.driver, wait).until_not(
                EC.element_to_be_clickable((By.ID, 'WAIT_win0'))
            )
        except TimeoutException:
            raise TimeoutException('Job search results did not not load')

if __name__ == "__main__":
    unittest.main()
