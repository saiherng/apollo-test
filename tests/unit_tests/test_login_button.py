import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import printFail, printPass, TestInfo

class TestLoginButtonUnitTest(unittest.TestCase):
    # Tests the input field for valid and invalid inputs

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver('http://127.0.0.1:3000')
    

    def test_EC005_valid_email_login(self):  
        testInfo = TestInfo("EC5", "Test Login button")

        email = "testa@gmail.com"
        
        login_box = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-input"]')

        login_box.send_keys(email)

        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/form/button")

        loginButton.click()

        userId = self.driver.getLocalStorage('userId')


        try:
            self.assertGreater(int(userId), 0)
            printPass(testInfo)
        except:
            printFail(testInfo)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


