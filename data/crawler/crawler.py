from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import logging


class Crawler:
    def __init__(self, config):
        self.config = config

        self._log_name = './logs/{}.log'.format(self.config.name.lower(), datetime.now().strftime('%Y.%m.%d.%H.%M.%S'))

        self.logger = logging.getLogger('crawler')
        logging.basicConfig(format='%(asctime)s [' + config.name + '] %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', filename=self._log_name)
        self.logger.setLevel(config.loggerStatus)

        self.driver = webdriver.Firefox()#(service_args=['--webdriver-logfile=' + self._log_name])
        self.actions = ActionChains(self.driver)
        self.keys = Keys

    def run(self):
        self.login()
        self.navigate()
        self.crawl()
        self.take_screen_shot()
        self.driver.close()

    def login(self):
        pass

    def navigate(self):
        pass

    def crawl(self):
        pass

    def take_screen_shot(self, name='screenshot'):
        self.driver.save_screenshot('./{}/{}.png'.format(self.config.name.lower(), name))
