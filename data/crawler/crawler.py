from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from datetime import datetime

import logging


class Crawler:
    def __init__(self, config):
        self.config = config

        self._log_name = './logs/{}.log'.format(datetime.now().strftime('%Y.%m.%d.%H.%M.%S'))

        self.logger = logging.getLogger('crawler')
        logging.basicConfig(format='%(asctime)s [' + config.name + '] %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', filename=self._log_name)
        self.logger.setLevel(config.loggerStatus)

        self.driver = webdriver.PhantomJS(service_args=['--web-security=no', '--webdriver-logfile=' + self._log_name])
        self.actions = ActionChains(self.driver)
        self.keys = Keys

    def run(self):
        try:
            self.login()
            self.navigate()
            self.crawl()
            self.driver.close()
        except Exception as e:
            self.take_screen_shot()
            raise e

    def login(self):
        pass

    def navigate(self):
        pass

    def crawl(self):
        pass

    def _wait_till_find_element_by(self, by, element_id, time=10):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((by, element_id))
            )

            return self.driver.find_element(by, element_id)

        except TimeoutException:
            self.logger.error('Could not find element: ' + element_id)
            raise TimeoutException('Could not find element: ' + element_id)

    def _switch_to_iframe(self, name, time=10):
        try:
            # Wait for iFrame to load (issue in PhantomJS)
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, name))
            )

            # Switch to job search iFrame and wait 10 seconds for search parameters to appear
            self.driver.switch_to.frame(self.driver.find_element_by_id(name))

        except TimeoutException:
            self.logger.error('Could not find iFrame: ' + name)
            raise TimeoutException('Could not find iFrame: ' + name)

    def take_screen_shot(self, name='screenshot'):
        self.driver.save_screenshot('./{}.png'.format(name))
