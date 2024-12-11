import time
import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import Env, printFail, printPass, TestInfo


class TestSessionSQLInjectionSecurityTest(unittest.TestCase):
    # Tests the Space Explorer page

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver(Env.domain)

    def test_EC033_login_field_sql_injection(self):
        testInfo = TestInfo("EC33", "Test login field against sql injection")

        login_box = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-input"]')
        
        self.driver.execute_script("arguments[0].scrollIntoView();", login_box)

        login_box.send_keys("test@gmail.com'-- DROP TABLE users;")
        time.sleep(1)

        login_box.submit()

        # re login with any user. If user table does not exist, it should not log in

        self.driver.login("test@gmail.com")

        # Verify that the user is logged in
        userId_ = self.driver.getLocalStorage('userId')

        
        try:
            self.assertGreater(int(userId_), 0)
            printPass(testInfo)
        except:
            testInfoError = TestInfo(testInfo.name, f"{testInfo.description}: Users table is deleted")
            printFail(testInfoError)

    def test_EC034_login_field_sql_injection(self):
        testInfo = TestInfo("EC34", "Test flights url against sql injection")

        self.driver.login("test@gmail.com")

        self.driver.driver.get(f"{Env.domain}/launch/109;'-- DROP TABLE users;")

        time.sleep(1)

        self.driver.logout()

        # re login with any user. If user table does not exist, it should not log in

        self.driver.login("test@gmail.com")

        # Verify that the user is logged in
        userId_ = self.driver.getLocalStorage('userId')

        
        try:
            self.assertGreater(int(userId_), 0)
            printPass(testInfo)
        except:
            testInfoError = TestInfo(testInfo.name, f"{testInfo.description}: Users table is deleted")
            printFail(testInfoError)

    
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()