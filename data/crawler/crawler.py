import os
import traceback
import time
import redis

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import shared.logger as logger
import shared.secrets as secrets


class Crawler:
    def __init__(self, config):
        self.config = config

        self.redis = redis.StrictRedis(host=secrets.REDIS_HOST, port=secrets.REDIS_PORT, db=secrets.REDIS_DB)

        self.logger = logger

        self._base_path = '{}/{}/'.format(os.path.dirname(os.path.abspath(__file__)), config.name.lower())
        self._log_name = '{}/logs/{}.log'.format(self._base_path, datetime.now().strftime('%Y.%m.%d.%H.%M.%S'))

        self.driver = webdriver.PhantomJS(service_args=['--web-security=no', '--webdriver-logfile=' + self._log_name])

        self.driver.implicitly_wait(self.config.crawler_interval)

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

    def wait_till_find_element_by(self, by, element_id, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((by, element_id))
            )

            return self.driver.find_element(by, element_id)

        except TimeoutException:
            self.logger.error(self.config.name, 'Could not find element: ' + element_id)
            raise TimeoutException('Could not find element: ' + element_id)

    def switch_to_iframe_by_id(self, iframe_id, wait=10):
        try:
            # Wait for iFrame to load (Sometimes an issue in PhantomJS)
            WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((By.ID, iframe_id))
            )

            self.driver.switch_to.frame(self.driver.find_element_by_id(iframe_id))

        except TimeoutException:
            self.logger.error(self.config.name, 'Could not find iFrame: ' + iframe_id)
            raise TimeoutException('Could not find iFrame: ' + iframe_id)

    def take_screen_shot(self, screenshot_name='screenshot'):
        self.driver.save_screenshot('{}/{}.png'.format(self._base_path, screenshot_name))
