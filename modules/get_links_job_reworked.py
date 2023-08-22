from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from load_django import *
from parser_job.models import *

class Linked:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        self.driver.maximize_window()


    def get_links(self, job):
        url = f'https://www.linkedin.com/jobs/search?keywords={job}&location=%D0%A1%D0%BE%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%A8%D1%82%D0%B0%D1%82%D1%8B%20%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B8&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
        self.driver.get(url)
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(3)

        all_links = self.driver.find_elements(By.XPATH, '//a[@data-tracking-control-name="public_jobs_jserp-result_search-card"]')

        for link in all_links:
            parse_link = link.get_attribute("href")
            parse_name = link.text

            obj, created = JobKeywords.objects.get_or_create(
                link = parse_link, 
                name = parse_name,
                status = 'New'
            )
        


if __name__ == '__main__':
    l = Linked()       
    l.get_links('architect')