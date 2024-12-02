import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ApolloSeleniumDriver():

    def __init__(self, link):

        self.driver = webdriver.Chrome()
        # self.driver.start_devtools()  
        # self.action = ActionChains(self.driver)

        self.driver.get(link)
        self.driver.implicitly_wait(10)
        self.cleanLocalStorate()

    
    def getCurrentUrl(self):
        return self.driver.current_url
    
    def getLocalStorage(self, key):
        return self.driver.execute_script(f"return window.localStorage.getItem('{key}')")

    def cleanLocalStorate(self):
        self.driver.execute_script("return window.localStorage.clear()")


    def find_element(self, by, value, timeout=1):

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    
    def back(self):
        self.driver.back()
    

    def execute_script(self,script, target):
        return self.driver.execute_script(script,target)
    
    def scrollIntoView(self, element):
        return self.execute_script("arguments[0].scrollIntoView();", element)

    def login(self, email):
        
        login_box = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-input"]')
        
        self.execute_script("arguments[0].scrollIntoView();", login_box)

        login_box.send_keys(email)

        login_box.submit()

    def select_rocket(self, path):

        sentinal = self.driver.find_element(By.XPATH, path)
        #self.driver.execute_script("arguments[0].scrollIntoView();", sentinal)
   
        time.sleep(1)
        sentinal.click()


    def add_to_cart(self):

        button = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="action-button"]')
        #self.driver.execute_script("arguments[0].scrollIntoView();", button)

        button.click()
        

    def go_to_cart(self):

        cart = self.driver.find_element(By.XPATH,'//*[@id="root"]/footer/div/a[2]')
        cart.click()

    def book_all(self):
        
        button = WebDriverWait(self.driver, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid=book-button]'))
        )
        if button.is_displayed():
            print("BUTTON EXISTS")
        button.click()


    def go_to_profile(self):
        
        profile = self.driver.find_element(By.XPATH,'//*[@id="root"]/footer/div/a[3]')
        profile.click()
 

    def logout(self):

        logout_button = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="logout-button"]')
        logout_button.click()

    
    


    def quit(self):
        self.driver.quit()


