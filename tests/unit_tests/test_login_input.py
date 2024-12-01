import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import printFail, printPass, TestInfo

class TestLoginInputUnitTest(unittest.TestCase):
    # Tests the input field for valid and invalid inputs

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver('http://127.0.0.1:3000')
    
    def _populateInputField(self, email):
        # Returns userId

        login_box = self.driver.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-input"]')

        login_box.send_keys(email)

        login_box.submit()

        return self.driver.getLocalStorage('userId')

    def test_EC001_valid_email_login(self):
        testInfo = TestInfo("EC1", "Test Login input field with valid email address")

        self.driver.cleanLocalStorate()

        email = "testa@gmail.com"
        
        userId = self._populateInputField(email)

        try:
            self.assertGreater(int(userId), 0)
            printPass(testInfo)
        except:
            printFail(testInfo)
    
    def test_EC002_invalid_email_login_string_only(self):
        testInfo = TestInfo("EC2", "Test Login input field with invalid email address: String only")

        self.driver.cleanLocalStorate()

        userId = self._populateInputField("test")

        try:
            self.assertIs(userId, None)
            printPass(testInfo)
        except:
            printFail(testInfo)
    
    def test_EC003_invalid_email_login_no_domain(self):
        testInfo = TestInfo("EC3", "Test Login input field with invalid email address: no domain")

        self.driver.cleanLocalStorate()

        userId = self._populateInputField("test@")

        try:
            self.assertIs(userId, None)
            printPass(testInfo)
        except:
            printFail(testInfo)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


