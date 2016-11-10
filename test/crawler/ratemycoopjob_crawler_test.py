import os
import time
import unittest


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import shared.ratemycoopjob as config


class RateMyCoopJobCrawler(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS(service_log_path=os.path.devnull, service_args=['--web-security=no'])
        self.driver.get(config.url)
        self.wait()

    def tearDown(self):
        self.driver.close()

    def test_elements_exists(self):
        all_jobs_ele = self.wait_till_find_element_by(By.ID, 'all_jobs_info')
        self.assertEqual(all_jobs_ele.tag_name, u'div')

        total_results = int(all_jobs_ele.text.split()[5])

        for i in range(1, total_results + 1):
            self.driver.get('http://www.ratemycoopjob.com/job/{}'.format(i))

            # Ratemycoopjob.com sometimes has errors when querying for certain jobs
            if len(self.driver.find_elements_by_css_selector('.dialog')) > 0:
                total_results += 1
                continue

            page_title = self.wait_till_find_element_by(By.CLASS_NAME, 'job_title').text.strip().split('at')

            employer_name = page_title[1].strip()
            job_title = page_title[0].strip()

            self.assertTrue(employer_name)
            self.assertTrue(job_title)

            rating_list = self.driver.find_elements_by_xpath("/div[@class='job_rating_box']")

            # Iterate through ratings which display comment, rating, salary etc.
            for rating in rating_list:
                rating_content = rating.find_element(By.CLASS_NAME, 'job_rating_content')
                self.assertEqual(rating_content.tag_name, u'div')

                job_rating_img_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating']/img[1]")
                self.assertEqual(job_rating_img_ele.tag_name, u'img')
                self.assertIn(u'stars', job_rating_img_ele.get_attribute('alt'))

                job_comment_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating_comment']")
                self.assertEqual(job_comment_ele.tag_name, u'div')

                job_comment_date_ele = job_comment_ele.find_element(By.XPATH, ".//span[@class='rating_date']/p[1]")
                self.assertEqual(job_comment_date_ele.tag_name, u'p')

                job_salary_ele = rating_content.find_element(By.XPATH, ".//div[@class='job_rating_salary_label']")
                self.assertEqual(job_salary_ele.tag_name, u'div')
                self.assertIn('Based on', job_salary_ele.text)
                self.assertIn('$', job_salary_ele.text)
                self.assertIn('/week', job_salary_ele.text)

            break

    @staticmethod
    def wait():
        time.sleep(config.crawler_interval)

    def wait_till_find_element_by(self, by, element_id, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((by, element_id))
            )

            return self.driver.find_element(by, element_id)
        except TimeoutException:
            raise TimeoutException('Could not find element: ' + element_id)

if __name__ == "__main__":
    unittest.main()
