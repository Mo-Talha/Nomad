import crawler
import config.jobmine as config


class JobmineCrawler(crawler.Crawler):
    def __init__(self):
        crawler.Crawler.__init__(self, config)

    def login(self):
        self.driver.get(config.url)
        self.driver.save_screenshot('test.png')
        self.driver.find_element_by_id('userid').send_keys(config.username)
        ele = self.driver.find_element_by_id('pwd')
        ele.send_keys(config.password)
        ele.send_keys(self.keys.ENTER)
        print self.driver.find_element_by_id('crefli_UW_CO_JOBSRCH_LINK').text

if __name__ == "__main__":
    jobmine_crawler = JobmineCrawler()
    jobmine_crawler.run()
