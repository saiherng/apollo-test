import time
import unittest

from selenium.webdriver.common.by import By

import sys
sys.path.append('..')
sys.path.append('../..')

from ApolloDriver import ApolloSeleniumDriver
from utils import Env, printFail, printPass, TestInfo


class TestLauchPageUnitTest(unittest.TestCase):
    # Tests the Space Explorer page

    def setUp(self):
        # Setup the Chrome WebDriver
        # Update with path
        self.driver = ApolloSeleniumDriver(Env.product_page)
    
    def test_EC011_page_content(self):
        testInfo = TestInfo("EC11", "Test that the page exists and content loaded")

        EXPECTED_LOGO_URL = "https://images2.imgbox.com/d2/3b/bQaWiil0_o.png"
        EXPECTED_TITLE = "Starlink-15 (v1.0)"
        EXPECTED_FLIGHT_NAME = "Falcon 9 (FT)"
        EXPECTED_FLIGHT_CAPTION = "CCAFS SLC 40"
        EXPECTED_FLIGHT_BANNER_IMAGE_URL = "/static/media/iss.85e97a3658472f796308.jpg"

        self.driver.login("test@gmail.com")

        logo = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/img")
        title = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/h2")
        flight_name = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/h3")
        flight_caption = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/h5")
        flight_banner = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]")

        try:
            try:
                logoUrl = logo.get_attribute('src')
                self.assertEqual(logoUrl, EXPECTED_LOGO_URL)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.1", "Incorrect Logo URL")
                printFail(subTestInfo)

            try:
                self.assertEqual(title.text, EXPECTED_TITLE)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.2", "Incorrect Title")
                printFail(subTestInfo)

            try:
                self.assertEqual(flight_name.text, EXPECTED_FLIGHT_NAME)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.3", "Incorrect Flight Name")
                printFail(subTestInfo)

            try:
                self.assertEqual(flight_caption.text, EXPECTED_FLIGHT_CAPTION)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.4", "Incorrect Flight Caption")
                printFail(subTestInfo)

            try:
                flightBannerStyle = flight_banner.get_attribute('style')
                containsImage = flightBannerStyle.find(EXPECTED_FLIGHT_BANNER_IMAGE_URL)
                self.assertGreater(containsImage, -1)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.5", "Incorrect Flight Banner Image")
                printFail(subTestInfo)
            
            printPass(testInfo)
        except:
            printFail(testInfo)

    def test_EC012_button_texts(self):
        testInfo = TestInfo("EC12", "Test Add To Cart Button Texts")

        EXPECTED_NOT_IN_CART_TEXT = "ADD TO CART"
        EXPECTED_IN_CART_TEXT = "REMOVE FROM CART"

        self.driver.login("test@gmail.com")

        button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="action-button"]')


        try:
            try: 
                # Test that correct text is loaded
                self.assertEqual(button.text, EXPECTED_NOT_IN_CART_TEXT)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.1", "Incorrect button text when not in cart")
                printFail(subTestInfo)
            
            # Test to add to cart
            button.click()
            try:
                # Test that button now reads correct text
                self.assertEqual(button.text, EXPECTED_IN_CART_TEXT)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.2", "Incorrect button text when in cart")
                printFail(subTestInfo)
            
            # Click to remove from cart
            button.click()

            try: 
                # Test that correct text is loaded
                self.assertEqual(button.text, EXPECTED_NOT_IN_CART_TEXT)
            except:
                subTestInfo = TestInfo(f"{testInfo.name}.3", "Incorrect button text when not in cart")
                printFail(subTestInfo)

            printPass(testInfo)
        except:
            printFail(testInfo)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()