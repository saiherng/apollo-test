import time
import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import printFail, printPass, TestInfo


class TestSpaceExplorerHeaderUnitTest(unittest.TestCase):
    # Tests the Space Explorer page

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver('http://127.0.0.1:3000')
    
    def test_EC4_email_address_on_header(self):
        # print("\n")
        # print("EC4: Test that the header shows the correct email address")
        testInfo = TestInfo("EC4", "Test that the header shows the correct email address")

        email = "test@gmail.com"

        self.driver.login(email)

        expectedEmail = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/h5")


        try:
            self.assertEqual(email, expectedEmail.text.lower())
            printPass(testInfo)
        except:
            printFail(testInfo)

    def test_EC5_flights_list(self):
        # print("\n")
        # print("EC5: Test that the page loads a list of 1 or more flights")
        testInfo = TestInfo("EC5", "Test that the page loads a list of 1 or more flights")

        self.driver.login("test@gmail.com")

        flighsList = self.driver.driver.find_elements(By.XPATH, "/html/body/div/div[2]/a")

        validIfLinkIsLaunch = False

        for flight in flighsList:
            link = flight.get_attribute('href')
            if link.find('/launch/') > 0:
                validIfLinkIsLaunch = True
                break
            
        try:
            self.assertTrue(validIfLinkIsLaunch)
            printPass(testInfo)
        except:
            printFail(testInfo)

    def test_EC6_flights_list_pagination(self):
        # print("\n")
        # print("EC6: Test that flight list paginates, and tests adds more button")

        testInfo = TestInfo("EC6", "Test that flight list paginates, and tests adds more button")
        EXPECTED_NUMBER_OF_LINKS = 20

        self.driver.login("test@gmail.com")

        numberOfFlights = self._countFlights()
            
        # First list, without pagination, should show expected number of links
        try:
            self.assertEqual(numberOfFlights, EXPECTED_NUMBER_OF_LINKS)
            printPass(testInfo)
        except:
            printFail(testInfo)

        # Now, add more flights
        addMoreButton = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/button")

        self.driver.execute_script("arguments[0].scrollIntoView();", addMoreButton)

        addMoreButton.click()

        time.sleep(3)

        # Reload list of flighs
        numberOfFlights = self._countFlights()

        # assert that the page now contains more than the initial number of links
        try:
            self.assertGreater(numberOfFlights, EXPECTED_NUMBER_OF_LINKS)
            printPass(testInfo)
        except:
            printFail(testInfo)

    def _countFlights(self):
        flighsList = self.driver.driver.find_elements(By.XPATH, "/html/body/div/div[2]/a")

        numberOfFlights = 0

        for flight in flighsList:
            link = flight.get_attribute('href')
            if link.find('/launch/') > 0:
                numberOfFlights += 1
        
        return numberOfFlights

    def test_EC7_single_flight_link(self):
        # print("\n")
        # print("EC7: Test that the flight link goes to flight page")

        testInfo = TestInfo("EC7", "Test that the flight link goes to flight page")
        EXPECTED_FLIGHT_PAGE_URL = "http://127.0.0.1:3000/launch/109"

        self.driver.login("test@gmail.com")

        # get first flight from the list
        flight = self.driver.driver.find_element(By.XPATH, "/html/body/div/div[2]/a[1]")

        flight.click()

        new_url = self.driver.driver.current_url

        try:
            self.assertEqual(new_url, EXPECTED_FLIGHT_PAGE_URL)
            printPass(testInfo)
        except:
            printFail(testInfo)
        
    
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()