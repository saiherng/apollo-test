import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppoloSeleniumDriver():

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.start_devtools()  
        # self.action = ActionChains(self.driver)

        self.driver.get('http://127.0.0.1:3000')


    def login(self, email):

        login_box = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/form/input')
        
        self.driver.execute_script("arguments[0].scrollIntoView();", login_box)
        time.sleep(1)

        login_box.send_keys(email)
        time.sleep(1)

        login_box.submit()


    def select_rocket(self, path):

        sentinal = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].scrollIntoView();", sentinal)
   
        time.sleep(1)
        sentinal.click()


    def add_to_cart(self):

        button = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="action-button"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        
        #Finding element by Xpath
        # launch = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/button')
        # self.driver.execute_script("arguments[0].scrollIntoView();", launch)
        #launch.click()

    def go_to_cart(self):

        cart = self.driver.find_element(By.XPATH,'//*[@id="root"]/footer/div/a[2]')
        cart.click()

    def book_all(self):
        
        button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid=book-button]'))
        )
        if button.is_displayed():
            print("BUTTON EXISTS")
        button.click()

        # CHECK IF BUTTON IS DISABLED
        # button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="book-button"]')
        # if button.get_attribute("disabled"):
        #     print("Button is disabled")
        # else:
        #     button.click()


    def go_to_profile(self):
        
        profile = self.driver.find_element(By.XPATH,'//*[@id="root"]/footer/div/a[3]')
        profile.click()
 

    def logout(self):

        logout_button = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="logout-button"]')
        logout_button.click()

    def quit(self):
        self.driver.quit()



def main():

    driver = AppoloSeleniumDriver()

    #COPY XPATH from browser and paste into this variable
    rocket_xpath = '//*[@id="root"]/div[2]/a[6]'

    email = 'test2@gmail.com'

    time.sleep(2)
    driver.login(email)

    time.sleep(2)
    driver.select_rocket(rocket_xpath)

    time.sleep(2)
    driver.add_to_cart()

    time.sleep(2)
    driver.go_to_cart()

    time.sleep(5)
    driver.book_all()

    time.sleep(1)
    driver.go_to_profile()

    time.sleep(2)
    driver.logout()

    time.sleep(2)
    driver.quit()



if __name__ == '__main__':
    main()




