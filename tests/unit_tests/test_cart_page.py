import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import Env, printFail, printPass, TestInfo

class TestCartPageUnitTest(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver(Env.cart_page)
    

    def test_EC018_test_cartpage_exists(self):  
        testInfo = TestInfo("EC18", "Test Cart Page Exists")
        
        self.driver.login("test@gmail.com")

        EXPECTED_PAGE_TITLE = "My Cart"

        try:
            pageTitle = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/h2')


            self.assertEqual(pageTitle.text, EXPECTED_PAGE_TITLE)

            printPass(testInfo)
        except:
            printFail(testInfo)

    def test_EC019_test_cart_is_not_accessible_without_sign_in(self):  
        testInfo = TestInfo("EC19", "Test Cart Page is not accessible without signin")

        try:
            # Verfiy the user is signed out
            userId = self.driver.getLocalStorage('userId')

            try:
                self.assertIsNone(userId)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.1", "User should not be logged in.")
                printFail(subTestInfo)

            self.driver.driver.get(Env.cart_page)

            loginInput = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-input"]')


            self.assertIsNotNone(loginInput)

            printPass(testInfo)
        except:
            printFail(testInfo)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


