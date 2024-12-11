import time
import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import Env, printFail, printPass, TestInfo


class TestUserDataLeak(unittest.TestCase):
    # Tests the Space Explorer page

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver(Env.domain)

    def test_EC035_user_data_leak(self):
        testInfo = TestInfo("EC35", "Test if users' booking are visible to other users")
        
        
        #login with user a
        self.driver.login('test@gmail.com')

        #book flight with user a
        self.driver.bookAFlight()

        #logout user a
        self.driver.logout()

        #login user b
        self.driver.login('test2@gmail.com')
        time.sleep(1)
        
        #validate if booking from user a exists on user b cart

        self.driver.driver.get(Env.profile_page)
        time.sleep(1)

        bookedFlights = self.driver.driver.find_elements(By.XPATH, '/html/body/div/div[2]/a')

        bookedFlightsIsFound = False

        for flight in bookedFlights:
            link = flight.get_attribute('href')

            if link == Env.product_page:
                bookedFlightsIsFound = True
                break

        try:
            self.assertFalse(bookedFlightsIsFound)
            printPass(testInfo)
        except:
            printFail(testInfo)


    
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()