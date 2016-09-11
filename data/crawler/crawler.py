from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import logging as logger


class Crawler:
    def __init__(self, config):
        self.config = config

        name = './logs/{}/{}.log'.format(config.name.lower(), datetime.now().strftime('%Y.%m.%d.%H.%M.%S'))
        self.driver = webdriver.Firefox()#(service_args=['--webdriver-logfile=' + name])

        self.keys = Keys
        self.logger = logger

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
        self.driver.save_screenshot(name + '.png')
