import time
import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import Env, printFail, printPass, TestInfo


class TestBookingIntegrationTest(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver(Env.domain)
    
    
    def test_EC028_book_one_flight(self):
        testInfo = TestInfo("EC28", "Test Book One Flight")

        self.driver.login('test@gmail.com')

        self.driver.driver.get(Env.home_page)

        EXPECTED_FLIGHT_URL = self._selectFlightFromList(1)

        self._goToCart()

        bookButton = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="book-button"]')

        bookButton.click()

        self.driver.driver.get(Env.profile_page)

        bookedFlights = self.driver.driver.find_elements(By.XPATH, '/html/body/div/div[2]/a')

        bookedFlightsIsFound = False

        for flight in bookedFlights:
            link = flight.get_attribute('href')

            if link == EXPECTED_FLIGHT_URL:
                bookedFlightsIsFound = True
                break

        try:
            self.assertTrue(bookedFlightsIsFound)
            printPass(testInfo)
        except:
            printFail(testInfo)
    
    def test_EC029_book_two_flights(self):
        testInfo = TestInfo("EC29", "Test Book Two Flights")

        self.driver.login('test@gmail.com')
        time.sleep(1)

        self.driver.driver.get(Env.home_page)

        selectedFlights = [
            self._selectFlightFromList(2),
            self._selectFlightFromList(3)
        ]

        self._goToCart()
        time.sleep(1)

        bookButton = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="book-button"]')
        self.driver.scrollIntoView(bookButton)
        bookButton.click()

        self.driver.driver.get(Env.profile_page)

        bookedFlights = self.driver.driver.find_elements(By.XPATH, '/html/body/div/div[2]/a')

        bookedFlightsAreFound = [False, False]

        foundIndex = 0
        for flight in bookedFlights:
            link = flight.get_attribute('href')

            if link == selectedFlights[0] or link == selectedFlights[1]:
                bookedFlightsAreFound[foundIndex] = True
                foundIndex += 1

        try:
            self.assertTrue(bookedFlightsAreFound[0])
            self.assertTrue(bookedFlightsAreFound[1])
            printPass(testInfo)
        except:
            printFail(testInfo)

    def test_EC030_test_remove_one_booking(self):
        testInfo = TestInfo("EC30", "Test Remove booked flight")

        self.driver.login('test@gmail.com')

        EXPECTED_FLIGHT_URL = Env.product_page
        EXPECTED_CANCEL_BUTTON_TEXT = "CANCEL THIS TRIP"

        try:
            # Verify the flight exists
            self.driver.driver.get(Env.profile_page)

            bookedFlights = self.driver.driver.find_elements(By.XPATH, '/html/body/div/div[2]/a')

            bookedFlightsIsFound = False

            for flight in bookedFlights:
                link = flight.get_attribute('href')

                if link == EXPECTED_FLIGHT_URL:
                    bookedFlightsIsFound = True
                    break

            try:
                self.assertTrue(bookedFlightsIsFound)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.1", "Can not complete because test is not booked. Book a test to continue")
                printFail(subTestInfo)

            self.driver.driver.get(EXPECTED_FLIGHT_URL)

            removeButton = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="action-button"]')

            try:
                self.assertEqual(removeButton.text, EXPECTED_CANCEL_BUTTON_TEXT)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.2", "Button does not read Cancel This Trip")
                printFail(subTestInfo)

            removeButton.click()

            self.driver.driver.get(Env.profile_page)

            bookedFlights = self.driver.driver.find_elements(By.XPATH, '/html/body/div/div[2]/a')

            bookedFlightsIsFound = False

            for flight in bookedFlights:
                link = flight.get_attribute('href')

                if link == EXPECTED_FLIGHT_URL:
                    bookedFlightsIsFound = True
                    break

            try:
                self.assertFalse(bookedFlightsIsFound)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.3", "Trip should not show in the booked flights")
                printFail(subTestInfo)

            printPass(testInfo)
        except:
            printFail(testInfo)

    def test_EC031_test_remove_one_booking(self):
        testInfo = TestInfo("EC31", "Test Remove all booked flights")

        self.driver.login('test@gmail.com')
        time.sleep(1)

        # Verify the flight exists
        self.driver.driver.get(Env.profile_page)

        bookedFlights = self.driver.driver.find_elements(By.XPATH, '/html/body/div/div[2]/a')

        bookedUrls = []

        for flight in bookedFlights:
            link = flight.get_attribute('href')
            bookedUrls.append(link)

        for bookedUrl in bookedUrls:
            self.driver.driver.get(bookedUrl)
            removeButton = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="action-button"]')
            self.driver.scrollIntoView(removeButton)
            removeButton.click()

        self.driver.driver.get(Env.profile_page)

        emptyFlightMessage = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/p')

        try:
            self.assertEqual(emptyFlightMessage.text, "You haven't booked any trips")
            printPass(testInfo)
        except:
            printFail(testInfo)
    

    def _goToCart(self):
        cartLink = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/cart"]')
        cartLink.click()

    def _goToHome(self):
        homeLink = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        homeLink.click()

    def _selectFlightFromList(self, id):
        self._goToHome()
        flight = self.driver.find_element(By.XPATH, f"/html/body/div/div[2]/a[{id}]")
        self.driver.scrollIntoView(flight)

        flightLink = flight.get_attribute('href')

        flight.click()
        addButton = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="action-button"]')
        self.driver.scrollIntoView(addButton)
        addButton.click()
        time.sleep(1)

        return flightLink

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()