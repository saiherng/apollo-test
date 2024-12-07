import time
import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import Env, printFail, printPass, TestInfo


class Test404RequestsUnitTest(unittest.TestCase):
    # Tests the Space Explorer page

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver(Env.domain)

    def test_EC024_test_not_existing_page_signed_in(self):  
        testInfo = TestInfo("EC24", "Test non existing page while signed in")
        
        self.driver.login("test@gmail.com")
        time.sleep(1)

        self.driver.driver.get(f"{Env.domain}/random-page-that-does-not-exist")


        try:
            pageContent = self.driver.find_element(By.XPATH, '/html/body/div/div[2]')

            childrenElements = pageContent.find_elements(By.CSS_SELECTOR, "*")

            elementCount = 0

            for _ in childrenElements:
                elementCount += 1

            self.assertEqual(elementCount, 0)

            printPass(testInfo)
        except:
            printFail(testInfo)
    
    def test_EC025_test_not_existing_page_signed_out(self):  
        testInfo = TestInfo("EC25", "Test non existing page while signed out")

        try:
            # Verfiy the user is signed out
            userId = self.driver.getLocalStorage('userId')

            try:
                self.assertIsNone(userId)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.1", "User should not be logged in.")
                printFail(subTestInfo)

            self.driver.driver.get(f"{Env.domain}/random-page-that-does-not-exist")

            loginInput = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-input"]')


            self.assertIsNotNone(loginInput)

            printPass(testInfo)
        except:
            printFail(testInfo)
        
    
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()