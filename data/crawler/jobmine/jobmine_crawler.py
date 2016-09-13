import data.crawler.crawler as crawler
import shared.jobmine as config
import shared.jobmine_data as data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime


class JobmineCrawler(crawler.Crawler):
    def __init__(self):
        crawler.Crawler.__init__(self, config)

    def login(self):
        self.driver.get(config.url)
        self.driver.find_element_by_id('userid').send_keys(config.username)
        pass_ele = self.driver.find_element_by_id('pwd')
        pass_ele.send_keys(config.password)
        pass_ele.send_keys(self.keys.ENTER)

    def navigate(self):
        try:
            job_search_ele_xpath = "(//li[@id='crefli_UW_CO_JOBSRCH_LINK']/a[1])[2]"

            # Wait for 10 seconds job search element to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, job_search_ele_xpath))
            )

            self.actions.move_to_element(self.driver.find_element_by_xpath(
                job_search_ele_xpath
            )).click().perform()

        except TimeoutException:
            self.logger.error('Job search link not found.')
            raise TimeoutException('Job search link not found')

    def crawl(self):
        self.set_search_params()
        pass

    def set_search_params(self):

        try:

            self._switch_to_iframe('ptifrmtgtframe')

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_JR'))
            )

        except TimeoutException:
            self.logger.error('Job search page did not not load.')
            raise TimeoutException('Job search page did not not load')

        else:
            coop_junior_ele = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_COOP_JR')
            coop_interm_ele = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_COOP_INT')
            coop_senior_ele = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_COOP_SR')
            coop_type_ele = self.driver.find_element_by_id('TYPE_COOP')

            if not coop_junior_ele.is_selected():
                coop_junior_ele.click()

            if not coop_interm_ele.is_selected():
                coop_interm_ele.click()

            if not coop_senior_ele.is_selected():
                coop_senior_ele.click()

            if not coop_type_ele.is_selected():
                coop_type_ele.click()

            coop_job_status_ele = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_JS_JOBSTATUS')

            for option in coop_job_status_ele.find_elements_by_tag_name('option'):
                if option.text == 'Posted':
                    option.click()
                    break

            now = datetime.now()

            # Get current term
            term = data.get_term(now.month)

            coop_term_ele = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_WT_SESSION')

            coop_term_ele.send_keys(data.term_data[now.year][term])

            coop_discipline_menu_1 = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_ADV_DISCP1')
            coop_discipline_menu_2 = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_ADV_DISCP2')
            coop_discipline_menu_3 = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_ADV_DISCP3')

            all_disciplines = coop_discipline_menu_1.find_elements_by_tag_name('option')

            disciplines_len = len(all_disciplines)

            search_ele = self.driver.find_element_by_id('UW_CO_JOBSRCHDW_UW_CO_DW_SRCHBTN')

            # Iterate through all disciplines
            for i, option in enumerate(all_disciplines):

                # Skip empty discipline
                if not option.get_attribute("value"):
                    continue

                # Select discipline 1
                option.click()

                # If next discipline exists, set it to discipline 2
                if 0 <= i + 1 < disciplines_len:
                    coop_discipline_menu_2.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP2']"
                                                                  "/option[@value='{}']"
                                                                  .format(all_disciplines[i + 1]
                                                                          .get_attribute("value"))).click()
                else:
                    coop_discipline_menu_2.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP2']"
                                                                  "/option[@value='']").click()
                # If next discipline exists, set it to discipline 3
                if 0 <= i + 2 < disciplines_len:
                    coop_discipline_menu_3.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP3']"
                                                                  "/option[@value='{}']"
                                                                  .format(all_disciplines[i + 2]
                                                                          .get_attribute("value"))).click()
                else:
                    coop_discipline_menu_3.find_element(By.XPATH, "//select[@id='UW_CO_JOBSRCH_UW_CO_ADV_DISCP3']"
                                                                  "/option[@value='']").click()

                # Initiate search
                search_ele.click()

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

                # Iterate through all jobs in current page
                for index in range(0, total_results):

                    employer_name = self.driver.find_element_by_id('UW_CO_JOBRES_VW_UW_CO_PARENT_NAME${}'.format(index)).text

                    job_title = self.driver.find_element_by_id('UW_CO_JOBTITLE_HL${}'.format(index)).text

                    location = self.driver.find_element_by_id('UW_CO_JOBRES_VW_UW_CO_WORK_LOCATN${}'.format(index)).text

                    openings = self.driver.find_element_by_id('UW_CO_JOBRES_VW_UW_CO_OPENGS${}'.format(index)).text

                    applicants = self.driver.find_element_by_id('UW_CO_JOBAPP_CT_UW_CO_MAX_RESUMES${}'.format(index)).text

                    self.driver.find_element_by_id('UW_CO_JOBTITLE_HL${}'.format(index)).click()

                    # Wait for new window to open containing job information
                    WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)

                    # Switch to new window
                    self.driver.switch_to.window(self.driver.window_handles[1])

                    self._switch_to_iframe('ptifrmtgtframe')

                    summary = self.driver.find_element_by_id('UW_CO_JOBDTL_VW_UW_CO_JOB_DESCR').text

                    self.driver.close()

                    # Wait for job window to close
                    WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 1)

                    # Switch back to job search page
                    self.driver.switch_to.window(self.driver.window_handles[0])

                    self._switch_to_iframe('ptifrmtgtframe')

                    print employer_name, job_title, location, openings, applicants, summary

                break

    def _switch_to_iframe(self, name, time=10):
        # Wait for iFrame to load (issue in PhantomJS)
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.ID, name))
        )

        # Switch to job search iFrame and wait 10 seconds for search parameters to appear
        self.driver.switch_to.frame(self.driver.find_element_by_id(name))

if __name__ == '__main__':
    jobmine_crawler = JobmineCrawler()
    jobmine_crawler.run()
