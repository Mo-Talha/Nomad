import re

from selenium.webdriver.common.by import By

import data.analysis.importer as importer
import data.crawler.crawler as crawler
import shared.ratemycoopjob as config


class RateMyCoopJobCrawler(crawler.Crawler):
    def __init__(self):
        crawler.Crawler.__init__(self, config)

    def login(self):
        self.driver.get(config.url)

        self.logger.info(self.config.name, 'Loaded {} homepage'.format(config.name))

    def navigate(self):
        self.wait()

    def crawl(self):
        self.logger.info(self.config.name, 'Loaded job search page')

        all_jobs_ele = self.wait_till_find_element_by(By.ID, 'all_jobs_info')

        total_results = int(all_jobs_ele.text.split()[5])

        self.logger.info(self.config.name, '{} results found'.format(total_results))

        self.logger.info(self.config.name, '*' * 10 + ' Beginning crawl ' + '*' * 10)

        # Iterate through all jobs
        for i in range(1, total_results + 1):
            self.driver.get('http://www.ratemycoopjob.com/job/{}'.format(i))

            # Ratemycoopjob.com sometimes has errors when querying for certain jobs
            if len(self.driver.find_elements_by_css_selector('.dialog')) > 0:
                dialog = self.driver.find_element_by_class_name('dialog')

                self.logger.info(self.config.name, 'Error while querying for job: {}. Returned: {}'
                                 .format(i, dialog.text))

                total_results += 1
                continue

            page_title = self.wait_till_find_element_by(By.CLASS_NAME, 'job_title').text.strip().split('at')

            employer_name = page_title[1].strip()
            job_title = page_title[0].strip()

            # Redis job key for ratemycoopjob crawler
            job_key = 'ratemycoopjob.{}.{}'.format(employer_name, job_title).replace(' ', '.')

            if not self.redis.exists(job_key):

                rating_list = self.driver.find_elements_by_xpath("//div[@class='job_rating_box']")

                comments = []

                # Iterate through ratings which display comment, rating, salary etc.
                for rating in rating_list:

                    rating_content = rating.find_element(By.CLASS_NAME, 'job_rating_content')

                    job_rating_img_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating']/img[1]")
                    job_comment_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating_comment']")
                    job_comment_date_ele = job_comment_ele.find_element(By.XPATH, ".//span[@class='rating_date']/p[1]")
                    job_salary_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating_salary_label']")

                    job_rating = float(job_rating_img_ele.get_attribute('alt').split('_')[0])

                    job_comment = re.search("\"(.*)\"", job_comment_ele.text).group(1)

                    job_comment_date = job_comment_date_ele.text

                    job_salary = float(job_salary_ele.text.replace('$', '').replace('/week', '')
                                       .replace('Based on', '')) / 40

                    comments.append({
                        'comment': job_comment,
                        'comment_date': job_comment_date,
                        'rating': job_rating,
                        'salary': job_salary
                    })

                importer.import_comment(employer_name=employer_name, job_title=job_title, comments=comments)

                self.redis.set(job_key, 1)
                self.redis.expire(job_key, self.config.cache_interval)

            else:
                self.logger.info(self.config.name, 'Job: {} from {} already exists in cache, skipping..'
                                 .format(job_title, employer_name))

            self.wait()
