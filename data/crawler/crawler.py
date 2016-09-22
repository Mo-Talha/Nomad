import os
import traceback
import time

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import shared.logger as logger


class Crawler:
    def __init__(self, config, importer):
        self.config = config
        self.importer = importer

        self._base_path = '{}/{}/'.format(os.path.dirname(os.path.abspath(__file__)),
                                          config.name.lower())

        self._log_name = '{}/logs/{}.log'.format(self._base_path, datetime.now().strftime('%Y.%m.%d.%H.%M.%S'))

        self.logger = logger

        self.driver = webdriver.PhantomJS(service_args=['--web-security=no', '--webdriver-logfile=' + self._log_name])
        self.driver.implicitly_wait(self.config.crawler_interval)

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
            error = traceback.format_exc()
            self.logger.error(self.config.name, error)
            print error
            raise e

    def login(self):
        pass

    def navigate(self):
        pass

    def crawl(self):
        pass

    def wait(self):
        self.logger.info(self.config.name, 'Waiting {} seconds'.format(self.config.crawler_interval))
        time.sleep(self.config.crawler_interval)

    def _wait_till_find_element_by(self, by, element_id, time=10):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((by, element_id))
            )

            return self.driver.find_element(by, element_id)

        except TimeoutException:
            self.logger.error(self.config.name, 'Could not find element: ' + element_id)
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
            self.logger.error(self.config.name, 'Could not find iFrame: ' + name)
            raise TimeoutException('Could not find iFrame: ' + name)

    def take_screen_shot(self, name='screenshot'):
        self.driver.save_screenshot('{}/{}.png'.format(self._base_path, name))
