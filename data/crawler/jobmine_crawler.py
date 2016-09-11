import crawler
import config.jobmine as config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class JobmineCrawler(crawler.Crawler):
    def __init__(self):
        crawler.Crawler.__init__(self, config)

    def login(self):
        self.driver.get(config.url)
        self.driver.find_element_by_id('userid').send_keys(config.username)
        ele = self.driver.find_element_by_id('pwd')
        ele.send_keys(config.password)
        ele.send_keys(self.keys.ENTER)

    def navigate(self):
        # Wait for 10 seconds job search element to appear
        try:
            search_ele_xpath = "(//li[@id='crefli_UW_CO_JOBSRCH_LINK']/a[1])[2]"

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, search_ele_xpath))
            )
            actions = ActionChains(self.driver)

            actions.move_to_element(self.driver.find_element_by_xpath(
                search_ele_xpath
            )).click().perform()

        except TimeoutException:
            print "Could not find job search link"


if __name__ == "__main__":
    jobmine_crawler = JobmineCrawler()
    jobmine_crawler.run()
