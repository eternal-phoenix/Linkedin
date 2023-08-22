import undetected_chromedriver as un
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LOGIN, PASSWORD
from selenium.common.exceptions import NoSuchElementException

from load_django import *
from parser_people.models import *


class SeleniumBot:
    
    def __init__(self):
        
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--enable-javascript')
        self.chrome_options.add_argument('--disable-gpu') 
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = un.Chrome(options=self.chrome_options) 

    
    def login(self):

        self.driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(LOGIN) 
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, "//button[@class='btn__primary--large from__button--floating']").send_keys(Keys.ENTER)
        time.sleep(15)
        

    def  get_info(self):

        for link_obj in PeopleLinks.objects.filter(status='Done'):

            self.driver.get(link_obj.link)
            print(link_obj.link)
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)

            try:
                name = self.driver.find_element(By.CSS_SELECTOR, 'h1.t-24').text.strip()
            except NoSuchElementException:
                name = None

            try:
                job = self.driver.find_element(By.CSS_SELECTOR, '.text-body-medium.break-words').text.strip()
            except NoSuchElementException:
                job = None


            try:
                geo = self.driver.find_element(By.XPATH, '//span[@class="text-body-small inline t-black--light break-words"]').text.strip()
            except NoSuchElementException:
                geo = None

            try:
                connections = self.driver.find_element(By.XPATH, '//*[@class="pv-top-card--list pv-top-card--list-bullet"]').text.strip()
            except NoSuchElementException:
                connections = None

            try:
                about = self.driver.find_element(By.XPATH, '//div[@class="pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center"]//span').text.strip()
            except NoSuchElementException:
                about = None
                
            try:
                educations = self.driver.find_elements(By.XPATH, "//section[.//div[@id='education']]//span[@class='t-14 t-normal']")
                educations = [item.text.strip() for item in educations if item]
            except NoSuchElementException:
                educations = None

            try:
                experiences = self.driver.find_elements(By.XPATH, '//section[.//div[@id="experience"]]//div[@class="display-flex flex-column full-width align-self-center"]')
                experiences = [item.text.strip().replace('\n', ' ') for item in experiences if item]
            except NoSuchElementException:
                experiences = None
            
            try:
                skils = self.driver.find_elements(By.CSS_SELECTOR, ".display-flex.align-items-center.mr1.hoverable-link-text.t-bold")
                skils = [item.text.strip().replace('\n', ' ') for item in skils if item]
            except NoSuchElementException:
                skils = None

            contacts_button = self.driver.find_element(by=By.ID, value='top-card-text-details-contact-info')
            self.driver.execute_script("window.scrollTo(0, 100)")
            contacts_button.click()
            time.sleep(2)
            contact_info = self.driver.find_element(by=By.XPATH, value='//section[@class="pv-profile-section pv-contact-info artdeco-container-card"]').text.strip().replace('Контактные сведения', '')

            defaults = {
                'name': name,
                'job': job,
                'geo': geo,
                'connections': connections,
                'about': about,
                'skils': skils,
                'education': educations,
                'experience': experiences, 
                'contact_info': contact_info, 
            }


            obj, created = PeopleInfo.objects.get_or_create(
                link = link_obj.link,
                defaults=defaults,
            )

            link_obj.status = 'Done'
            link_obj.save()

            # print(
            #     f'name {name}', 
            #     f'job {job}', 
            #     f'geo {geo}', 
            #     f'connections {connections}', 
            #     f'about {about}', 
            #     f'educations {educations}', 
            #     f'experiences {experiences}', 
            #     f'skils {skils}', 
            #     sep='\n'
            # )


def main():
    
    bot = SeleniumBot()
    bot.login()
    bot.get_info()


if __name__ == '__main__':
    main()

