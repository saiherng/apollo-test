import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import Env, printFail, printPass, TestInfo

class TestProfileButtonUnitTest(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.init_url = Env.product_page
        self.driver = ApolloSeleniumDriver(self.init_url)
    

    def test_EC014_test_profile_button(self):  
        testInfo = TestInfo("EC14", "Test Profile Button Navigation")

        EXPECTED_URL = Env.profile_page
        
        self.driver.login("test@gmail.com")

        try:
            # Verify that the current url is the logged in one
            self.assertEqual(self.driver.getCurrentUrl(), self.init_url)

            # Get the link to test
            profileLink = self.driver.find_element(By.XPATH, "/html/body/div/footer/div/a[3]")
            
            profileLink.click()

            self.assertEqual(self.driver.getCurrentUrl(), EXPECTED_URL)

            printPass(testInfo)
        except:
            printFail(testInfo)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


