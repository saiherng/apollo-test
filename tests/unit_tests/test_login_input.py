import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver

class TestLoginInputUnitTest(unittest.TestCase):
    # Tests the input field for valid and invalid inputs

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver('http://127.0.0.1:3000')
    
    def _populateInputField(self, email):
        # Returns userId

        login_box = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-input"]')

        login_box.send_keys(email)

        login_box.submit()

        self.driver.driver.implicitly_wait(1)

        return self.driver.getLocalStorage('userId')

    def test_EC1_valid_email_login(self):  
        print("\n")
        print("EC1: Test Login input field with valid email address")

        email = "testa@gmail.com"
        
        userId = self._populateInputField(email)

        self.assertGreater(int(userId), 0)
    
    def test_EC2_invalid_email_login_string_only(self):
        print("\n")
        print("EC2: Test Login input field with invalid email address: String only")

        email = "test"

        userId = self._populateInputField(email)

        self.assertIs(userId, None)
    
    def test_EC3_invalid_email_login_no_domain(self):
        print("\n")
        print("EC3: Test Login input field with invalid email address: no domain")

        email = "test@"

        userId = self._populateInputField(email)

        self.assertIs(userId, None)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


