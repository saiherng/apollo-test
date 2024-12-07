import time
import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import Env, printFail, printPass, TestInfo


class TestSessionCloneSecurityTest(unittest.TestCase):
    # Tests the Space Explorer page

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver(Env.domain)

    def test_EC032_clone_session(self):
        testInfo = TestInfo("EC32", "Test loging with stolen token")

        self.driver.login("test@gmail.com")

        # Steal the token and user id

        tokenValue = self.driver.getLocalStorage('token')
        userIdValue = self.driver.getLocalStorage('userId')


        self.driver.logout()

        # Verify that the user is logged out
        userId_ = self.driver.getLocalStorage('userId')

        self.assertIs(userId_, None)

        # put the token back into localstorage

        self.driver.setLocalStorage('token', tokenValue)
        self.driver.setLocalStorage('userId', userIdValue)

        # try to book a trip for the hacked user
        isBooked = self.driver.bookAFlight()

        try:
            self.assertFalse(isBooked)
            printPass(testInfo)
        except:
            testInfoError = TestInfo(testInfo.name, f"{testInfo.description}: Product should not " +
                                     "have been added to cart because session doest not was not "+
                                     "properly created")
            printFail(testInfoError)



    def _goToHome(self):
        homeLink = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        homeLink.click()

    
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()