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

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with your path to ChromeDriver
        self.driver = ApolloSeleniumDriver(Env.domain)
        
      

    def test_add_to_cart(self):

        self.email = "test@gmail.com"
        self.driver.login(self.email)

        #clicks on rocket
        self.path = '//*[@id="root"]/div[2]/a[1]'
        self.driver.select_rocket(self.path)

        time.sleep(2)
        #add to cart
        self.driver.add_to_cart()
        time.sleep(2)

        self.driver.go_to_cart()
        time.sleep(10)

       
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
