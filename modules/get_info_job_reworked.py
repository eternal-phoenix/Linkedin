from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By

from load_django import *
from parser_job import models
from time import sleep

class SeleniumBot:
    def __init__(self):
        self.DEBUG = False
        self.service = Service(ChromeDriverManager().install())
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        self.driver.maximize_window()


    def parse_data(self, kw_obj: models.JobKeywords):
            
        self.driver.get(kw_obj.link)
        print(f'\n[INFO] processing... {kw_obj.link}\n')
        sleep(2)

        if 'Join LinkedIn' in self.driver.page_source:
            print('\n[INFO] avoiding login ...\n')
            sleep(5)
            return True
        
        try:
            vacancy = self.driver.find_element(By.TAG_NAME, "h1").text.strip()
        except NoSuchElementException:
            vacancy = None

        try:
            name_company = self.driver.find_element(By.XPATH, '//a[@data-tracking-control-name="public_jobs_topcard-org-name"]').text.strip()
        except NoSuchElementException:
            name_company = None

        try:
            geo = self.driver.find_element(By.XPATH, '//span[@class="topcard__flavor topcard__flavor--bullet"]').text.strip()
        except NoSuchElementException:
            geo = None

        try:
            about_vacancy = self.driver.find_element(By.XPATH, '//section[@class="show-more-less-html"]//div').text.replace('\n', ' ').strip()
        except NoSuchElementException:
            about_vacancy = None

        employment_type, seniority_level, job_functions, industries = None, None, None, None

        try:
            additional_data = self.driver.find_elements(By.XPATH, '//ul[@class="description__job-criteria-list"]//li')
        except NoSuchElementException:
            additional_data = []
            print('\n[INFO] no additional data availiable...\n')
            
        for item in additional_data:
            try:
                item.find_element(By.XPATH, './/h3[contains(text(), "Employment type")]')
                employment_type = item.find_element(By.TAG_NAME, 'span').text.strip()
            except NoSuchElementException:
                pass
        
            try:
                item.find_element(By.XPATH, './/h3[contains(text(), "Seniority level")]')
                seniority_level = item.find_element(By.TAG_NAME, 'span').text.strip()
            except NoSuchElementException:
                pass 
        
            try:
                item.find_element(By.XPATH, './/h3[contains(text(), "Job function")]')
                job_functions = item.find_element(By.TAG_NAME, 'span').text.strip() 
            except NoSuchElementException:
                pass 
        
            try:
                item.find_element(By.XPATH, './/h3[contains(text(), "Industries")]')
                industries = item.find_element(By.TAG_NAME, 'span').text.strip() 
            except NoSuchElementException:
                pass 

        if self.DEBUG == True:
            print('\n', vacancy, name_company, geo, about_vacancy, seniority_level, employment_type, job_functions, industries, sep='\n')

        defaults = {
            'vacancy': vacancy,
            'name_company': name_company,
            'geo': geo,
            'about_vacancy': about_vacancy,
            'seniority_level': seniority_level, 
            'employment_type': employment_type, 
            'job_functions': job_functions, 
            'industries': industries,
        }
        obj, created = models.JobInfo.objects.get_or_create( link = kw_obj.link, defaults=defaults)

        kw_obj.status = "Done"
        kw_obj.save()

        
    def kill_bot(self):
        self.driver.close()
        self.driver.quit()


def run_bot():
    bot = SeleniumBot()
    
    for keyword_object in models.JobKeywords.objects.filter(status="New"):
        response = bot.parse_data(keyword_object)
        while response:
            response = bot.parse_data(keyword_object)

    bot.kill_bot()


if __name__ == '__main__':       
    run_bot()

        





