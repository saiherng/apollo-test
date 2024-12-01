import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import printFail, printPass, TestInfo

class TestHomeButtonUnitTest(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.init_url = 'http://127.0.0.1:3000/launch/109'
        self.driver = ApolloSeleniumDriver(self.init_url)
    

    def test_EC010_test_home_button(self):  
        testInfo = TestInfo("EC10", "Test Home Button Navigation")

        EXPECTED_URL = "http://127.0.0.1:3000/"
        
        self.driver.login("test@gmail.com")

        try:
            # Verify that the current url is the logged in one
            self.assertEqual(self.driver.getCurrentUrl(), self.init_url)

            # Get the link to test
            homeLink = self.driver.find_element(By.XPATH, "/html/body/div/footer/div/a[1]")
            
            homeLink.click()

            self.assertEqual(self.driver.getCurrentUrl(), EXPECTED_URL)

            printPass(testInfo)
        except:
            printFail(testInfo)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


