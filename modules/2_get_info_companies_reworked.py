from selenium import webdriver
import undetected_chromedriver as un
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from config import LOGIN, PASSWORD

from load_django import *
from parser_company.models import *



class Linked:

    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--enable-javascript')
        chrome_options.add_argument('--disable-gpu') 
        self.driver = un.Chrome(options=chrome_options) 

    def login(self):

        self.driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(LOGIN)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, "//button[@class='btn__primary--large from__button--floating']").send_keys(Keys.ENTER)
        time.sleep(30)
        print('\n[INFO] Logged in...\n')

    
    def get_company_info(self):
        print('\n[INFO] Getting companies info...\n')
        for l in CompaniesKeywords.objects.filter(status='New'):
            
            if ("company" in l.link):
                link = f'{l.link}about/'
                self.driver.get(link)
                time.sleep(5)
                # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))

                company_name = self.driver.find_element(By.XPATH, "//h1").text
                
                try:
                    company_website = self.driver.find_element(
                        By.XPATH, "//dt[text()='Website']/following-sibling::dd[1]").text
                except:
                    company_website = None
                
                try:
                    company_size = self.driver.find_element(
                        By.XPATH, "//dt[text()='Company size']/following-sibling::dd[1]").text
                except:
                    company_size = None
            
                try:    
                    industry = self.driver.find_element(
                        By.XPATH, "//dt[text()='Industry']/following-sibling::dd[1]").text.split(",")
                except:
                    industry = None
            
                try:
                    company_founded = self.driver.find_element(
                        By.XPATH, "//dt[text()='Founded']/following-sibling::dd[1]").text
                except:
                    company_founded = None
            
                try:
                    company_specialties = self.driver.find_element(
                        By.XPATH, "//dt[text()='Specialties']/following-sibling::dd[1]").text.split(",")
                except:
                    company_specialties = None
            
                try:
                    company_headquarters = self.driver.find_element(
                        By.XPATH, '//dt[text()="Headquarters"]/following-sibling::dd[1]').text.strip()
                except:
                    company_headquarters = None

                try:
                    overview = self.driver.find_element(
                        By.CSS_SELECTOR, "p.break-words").text
                except:
                    overview = None

                try:
                    ipo = self.driver.find_element(
                        By.XPATH, '//div[@class="org-funding__card-spacing"]//section//a[@class="ember-view link-without-hover-visited"]').get_attribute('href').strip()
                except:
                    ipo = None
                try:
                    nasdaq = self.driver.find_element(
                        By.CSS_SELECTOR, ".org-stock-quote__content-spacing .text-display-medium").text
                except:
                    nasdaq = None

                try:
                    programs = self.driver.find_element(By.CSS_SELECTOR, ".org-commitments-module__card-spacing .org-commitment-programs__text").text
                except:
                    programs = None  

                try:
                    learning = self.driver.find_element(By.CSS_SELECTOR, ".org-commitments-module__card-spacing .lt-line-clamp__raw-line").text
                except:
                    learning = None
                
                try:
                    location = self.driver.find_element(By.CSS_SELECTOR, ".org-location-card.pv2").text.replace('Primary', '').split('Get directions')[0]
                except:
                    location = None

                try:
                    phone = self.driver.find_element(By.XPATH, "//dt[text()='Phone']/following-sibling::dd[1]").text
                except:
                    phone = None 
                    
                
                jobs_link = f'{l.link}jobs/'
                self.driver.get(jobs_link)
                time.sleep(2)
                try:
                    job_actual = self.driver.find_element(
                        By.CSS_SELECTOR, "h4.org-jobs-job-search-form-module__headline").text
                    job_actual = ''.join(filter(str.isdigit, job_actual))
                except:
                    job_actual = None
            
                defaults = {
                    'company_name': company_name,
                    'company_website': company_website,
                    'company_size': company_size,
                    'company_founded': company_founded,
                    'company_specialties': company_specialties,
                    'industry': industry,
                    'company_headquarters': company_headquarters,
                    'overview': overview,
                    'ipo': ipo,
                    'nasdaq': nasdaq,
                    'programs': programs,
                    'learning': learning,
                    'job_actual': job_actual,
                    'location': location,
                    'phone': phone
                }

                print(
                    f'company_name: {company_name}', 
                    f'company_website: {company_website}', 
                    f'company_size: {company_size}', 
                    f'company_founded: {company_founded}', 
                    f'company_specialties: {company_specialties}', 
                    f'industry: {industry}', 
                    f'company_headquarters: {company_headquarters}', 
                    f'overview: {overview}', 
                    f'ipo: {ipo}', 
                    f'programs: {programs}', 
                    f'learning: {learning}', 
                    f'job_actual: {job_actual}', 
                    f'location: {location}', 
                    f'phone: {phone}', 
                    sep='\n'
                )

                obj, created = CompanyInfo.objects.get_or_create(
                    link = link,
                    defaults=defaults,
                )

                # l.status = 'Done'
                # l.save()

                time.sleep(2)


bot = Linked()
bot.login()
bot.get_company_info()

# for item in CompaniesKeywords.objects.all():
#     item.status = 'New'
#     item.save()