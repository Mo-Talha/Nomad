from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging as logger


class Crawler:
    def __init__(self, config):
        self.config = config
        self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any',
                                                        '--web-security=false'])
        self.keys = Keys
        self.logger = logger
        self.logger.basicConfig(filename='test.log', level=config.loggerStatus)

    def run(self):
        self.login()
        self.navigate()
        self.crawl()

    def login(self):
        pass

    def navigate(self):
        pass

    def crawl(self):
        pass
