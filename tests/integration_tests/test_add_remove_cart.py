import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import printFail, printPass, TestInfo


class TestAddRemoveCartIntegrationTest(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver('http://127.0.0.1:3000/launch/109')
    
    
    def test_EC015_add_to_cart(self):
        testInfo = TestInfo("EC15", "Test Add To Cart Button Action")

        EXPECTED_FLIGHT_URL = "http://127.0.0.1:3000/launch/109"

        self.driver.login("test@gmail.com")

        button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="action-button"]')


        try:
            button.click()

            self._goToCart()

            elementInCart = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/a")

            elementInCartUrl = elementInCart.get_attribute('href')

            self.assertEqual(elementInCartUrl, EXPECTED_FLIGHT_URL)

            printPass(testInfo)
        except:
            printFail(testInfo)
    
    def test_EC016_remove_from_cart(self):
        testInfo = TestInfo("EC16", "Test Remove From Cart Button Action")

        EXPECTED_FLIGHT_URL = "http://127.0.0.1:3000/launch/109"
        EXPECTED_CART_EMPTY_MESSAGE = "No items in your cart"

        self.driver.login("test@gmail.com")

        try:
            # add a product to cart
            button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="action-button"]')
            button.click()

            self._goToCart()

            # verify that the product is in cart
            elementInCart = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/a")
            elementInCartUrl = elementInCart.get_attribute('href')
            self.assertEqual(elementInCartUrl, EXPECTED_FLIGHT_URL)

            # Go Back to product page in order to remove product
            elementInCart.click()

            # Verify that the browser is at the product's page
            self.assertEqual(self.driver.getCurrentUrl(), EXPECTED_FLIGHT_URL)

            # Find the add to cart button
            addToCartButton = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="action-button"]')

            # Click the add to cart button to remove the product from cart
            addToCartButton.click()

            self._goToCart()

            # Cart should be empty now
            emptyMessage = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="empty-message"]')

            self.assertEqual(emptyMessage.text, EXPECTED_CART_EMPTY_MESSAGE)

            printPass(testInfo)
        except:
            printFail(testInfo)

    def _goToCart(self):
        cartLink = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/cart"]')
        cartLink.click()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()