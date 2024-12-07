import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys

from utils import Env
sys.path.append('..')

from ApolloDriver import ApolloSeleniumDriver

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with your path to ChromeDriver
        self.driver = ApolloSeleniumDriver(Env.domain)
       

    def test_valid_email_login(self):
    
        self.email = "test@gmail.com"
        self.driver.login(self.email)
        

        #Get email account banner
        self.email_banner = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/h5')

        #Test
        self.assertEqual(self.email, self.email_banner.text)

    
       
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
