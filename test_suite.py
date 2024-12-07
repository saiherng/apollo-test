import sys
import os


utils_path = os.path.abspath('tests')
utils_path_unit = os.path.abspath('tests/unit_tests')
utils_path_integration = os.path.abspath('tests/integration_tests')
sys.path.append(utils_path)
sys.path.append(utils_path_unit)
sys.path.append(utils_path_integration)

import unittest

from test_login_input import TestLoginInputUnitTest
from test_space_explorer_page import TestSpaceExplorerHeaderUnitTest
from test_launch_page import TestLauchPageUnitTest
from test_home_button import TestHomeButtonUnitTest
from test_cart_button import TestCartButtonUnitTest
from test_profile_button import TestProfileButtonUnitTest
from test_logout_button import TestLogoutButtonUnitTest
from test_add_remove_cart import TestAddRemoveCartIntegrationTest
from test_login_button import TestLoginButtonUnitTest

# from test_login import TestLogin
# from test_add_to_cart import TestAddToCart

def suite():
    test_suite = unittest.TestSuite()

    # ECs: Testing of Login Input Field
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLoginInputUnitTest))
    
    # ECs: Testing of Login Button
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLoginButtonUnitTest))

    # ECs: Testing of Space Explorer Page
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSpaceExplorerHeaderUnitTest))
    
    # ECs: Testing of Launch Page
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLauchPageUnitTest))
    
    # ECs: Testing of Footer Button Home
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHomeButtonUnitTest))
    
    # ECs: Testing of Footer Button Cart
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCartButtonUnitTest))
    
    # ECs: Testing of Footer Button Profile
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestProfileButtonUnitTest))
    
    # ECs: Testing of Footer Button Logout
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogoutButtonUnitTest))

    # Integration Tests

    # ECs: Testing of add to cart integration
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddRemoveCartIntegrationTest))

    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddToCart))


    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())