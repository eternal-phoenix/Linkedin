import undetected_chromedriver as un
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from config import LOGIN, PASSWORD

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
        

    def  get_links(self, query: str) -> None:

        url = f'https://www.linkedin.com/search/results/people/?keywords={query}&origin=SWITCH_SEARCH_VERTICAL&page=1&searchId=eec68627-2fdf-44b3-987e-43893307c575&sid=!Ml'
        self.driver.get(url)
        time.sleep(5)

        current_page = self.driver.current_url
        while True:
            try:
                self.parse_page()
            except NoSuchElementException:
                print('[INFO] search result is empty, try another query...')
                return False
            self.driver.find_element(by=By.XPATH, value='//button[@aria-label="Next"]').click()
            time.sleep(2)
            if self.driver.current_url == current_page:
                break
            current_page = self.driver.current_url        


    def parse_page(self):

        time.sleep(2)
        next_page = self.driver.find_element(By.XPATH, '//button[@aria-label="Next"]')
        self.driver.execute_script('arguments[0].scrollIntoView(true);', next_page)
        time.sleep(2)

        links = self.driver.find_elements(By.XPATH, '//a[@class="app-aware-link "]')[1:]
        for link in links:
            href = link.get_attribute("href")
            print(href)

            obj, created = PeopleLinks.objects.get_or_create(link=href, status='New')
           

def main():
    
    bot = SeleniumBot()
    bot.login()
    bot.get_links('designer 3d')


if __name__ == '__main__':
    main()