import re

import data.crawler.crawler as crawler
import shared.ratemycoopjob as config

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class RateMyCoopJobCrawler(crawler.Crawler):
    def __init__(self, importer):
        crawler.Crawler.__init__(self, config, importer)

    def login(self):
        self.driver.get(config.url)

        self.logger.info(self.config.name, 'Loaded {} homepage'.format(config.name))

    def navigate(self):
        self.wait()

    def crawl(self):
        self.logger.info(self.config.name, 'Loaded job search page')

        total_results = int(self._wait_till_find_element_by(By.ID, 'all_jobs_info').text.split()[5])

        self.logger.info(self.config.name, '{} results found'.format(total_results))

        self.logger.info(self.config.name, '*' * 10 + ' Beginning crawl ' + '*' * 10)

        # Iterate through all jobs
        for i in range(1, total_results + 1):
            self.driver.get('http://www.ratemycoopjob.com/job/{}'.format(i))

            # Ratemycoopjob.com sometimes has errors when querying for certain jobs
            try:
                dialog = self.driver.find_element_by_class_name('dialog')
            except NoSuchElementException:
                pass
            else:
                self.logger.info(self.config.name, 'Error while querying for job: {}. Returned: {}'
                                 .format(i, dialog.text))
                continue

            title = self._wait_till_find_element_by(By.CLASS_NAME, 'job_title').text.split('at')

            job_title = title[0].strip()
            employer_name = title[1].strip()

            rating_list = self._wait_till_find_element_by(By.ID, 'job_rating_list')\
                .find_elements_by_xpath("//div[@class='job_rating_box']")

            # Iterate through ratings which display comment, rating, salary etc.
            for rating in rating_list:
                rating_content = rating.find_element(By.CLASS_NAME, 'job_rating_content')

                job_rating_img_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating']/img[1]")
                job_comment_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating_comment']")
                job_comment_date_ele = job_comment_ele.find_element(By.XPATH, ".//span[@class='rating_date']/p[1]")
                job_salary_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating_salary_label']")

                job_rating = job_rating_img_ele.get_attribute('alt').split('_')[0]

                job_comment_text = job_comment_ele.text

                # TODO: fix regex
                job_comment = re.search("([\"'])(?:(?=(\\?))\2.)*?\1", job_comment_text)

                job_comment_date = job_comment_date_ele.text

                job_salary = job_salary_ele.text

                print job_rating, job_comment, job_comment_date, job_salary

            self.wait()

if __name__ == '__main__':
    ratemycoopjob_crawler = RateMyCoopJobCrawler(None)
    ratemycoopjob_crawler.run()
