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
    

    def test_EC015_test_logout_button(self):  
        testInfo = TestInfo("EC15", "Test Cart Page")
        
        self.driver.login("test@gmail.com")

        EXPECTED_PAGE_TITLE = "My Cart"

        try:
            pageTitle = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/h2')


            self.assertEqual(pageTitle.text, EXPECTED_PAGE_TITLE)

            printPass(testInfo)
        except:
            printFail(testInfo)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


