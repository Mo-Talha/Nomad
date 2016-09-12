import data.crawler.crawler
import data.crawler.config.jobmine as config
import util
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime


class JobmineCrawler(data.crawler.crawler.Crawler):
    def __init__(self):
        data.crawler.crawler.Crawler.__init__(self, config)

    def login(self):
        self.driver.get(config.url)
        self.driver.find_element_by_id('userid').send_keys(config.username)
        ele = self.driver.find_element_by_id('pwd')
        ele.send_keys(config.password)
        ele.send_keys(self.keys.ENTER)

    def navigate(self):
        try:
            search_ele_xpath = "(//li[@id='crefli_UW_CO_JOBSRCH_LINK']/a[1])[2]"

            # Wait for 10 seconds job search element to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, search_ele_xpath))
            )

            self.actions.move_to_element(self.driver.find_element_by_xpath(
                search_ele_xpath
            )).click().perform()

        except TimeoutException:
            self.logger.error('Job search link not found.')
            raise TimeoutException('Job search link not found')

    def crawl(self):
        self.set_search_params()
        pass

    def set_search_params(self):

        try:
            self.driver.switch_to.frame(self.driver.find_element_by_id('ptifrmtgtframe'))
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'UW_CO_JOBSRCH_UW_CO_COOP_JR'))
            )

        except TimeoutException:
            self.logger.error('Job search page did not not load.')
            raise TimeoutException('Job search page did not not load')

        else:
            coop_junior = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_COOP_JR')
            coop_interm = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_COOP_INT')
            coop_senior = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_COOP_SR')
            coop_radio = self.driver.find_element_by_id('TYPE_COOP')

            if not coop_junior.is_selected():
                coop_junior.click()

            if not coop_interm.is_selected():
                coop_interm.click()

            if not coop_senior.is_selected():
                coop_senior.click()

            if not coop_radio.is_selected():
                coop_radio.click()

            job_status = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_JS_JOBSTATUS')

            for option in job_status.find_elements_by_tag_name('option'):
                if option.text == 'Posted':
                    option.click()
                    break

            # Fall = September - December, Winter = January - April, Spring = May - August
            now = datetime.now()

            term = self._get_term(now.month)
            coop_term = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_WT_SESSION')

            coop_term.send_keys(util.term_data[now.year][term])

            discipline_menu = self.driver.find_element_by_id('UW_CO_JOBSRCH_UW_CO_ADV_DISCP1')

            for option in discipline_menu.find_elements_by_tag_name('option'):
                print option.get_attribute("value"), option.text

    @staticmethod
    def _get_term(month):
        term = ''
        if 1 <= month <= 4:
            term = 'Winter'
        elif 5 <= month <= 8:
            term = 'Spring'
        elif 9 <= month <= 12:
            term = 'Fall'

        return term

if __name__ == '__main__':
    jobmine_crawler = JobmineCrawler()
    jobmine_crawler.run()
