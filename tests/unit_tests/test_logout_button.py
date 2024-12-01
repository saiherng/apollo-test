import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import printFail, printPass, TestInfo

class TestLogoutButtonUnitTest(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.init_url = 'http://127.0.0.1:3000/launch/109'
        self.driver = ApolloSeleniumDriver(self.init_url)
    

    def test_EC013_test_logout_button(self):  
        testInfo = TestInfo("EC13", "Test Logout Button Navigation")

        EXPECTED_URL = "http://127.0.0.1:3000/"
        
        self.driver.login("test@gmail.com")

        try:
            # Verify that the user is logged in
            userId = self.driver.getLocalStorage('userId')

            self.assertGreater(int(userId), 0)

            # Get the link to test
            logoutButton = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="logout-button"]')
            
            logoutButton.click()

            # Verify that the user is logged out
            userId = self.driver.getLocalStorage('userId')

            self.assertIs(userId, None)

            printPass(testInfo)
        except:
            printFail(testInfo)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


