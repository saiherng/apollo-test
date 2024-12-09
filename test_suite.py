import sys
import os



utils_path = os.path.abspath('tests')
utils_path_unit = os.path.abspath('tests/unit_tests')
utils_path_integration = os.path.abspath('tests/integration_tests')
sys.path.append(utils_path)
sys.path.append(utils_path_unit)
sys.path.append(utils_path_integration)

import unittest
import sys

from test_login_input import TestLoginInputUnitTest
from test_home_page import TestSpaceExplorerHeaderUnitTest
from test_launch_page import TestLauchPageUnitTest
from test_home_button import TestHomeButtonUnitTest
from test_cart_button import TestCartButtonUnitTest
from test_profile_button import TestProfileButtonUnitTest
from test_logout_button import TestLogoutButtonUnitTest
from test_add_remove_cart import TestAddRemoveCartIntegrationTest
from test_login_button import TestLoginButtonUnitTest
from test_cart_page import TestCartPageUnitTest
from test_profile_page import TestProfilePageUnitTest
from test_booking import TestBookingIntegrationTest
from test_404_requests import Test404RequestsUnitTest
from tests.security_tests.test_session_clone import TestSessionCloneSecurityTest



# from test_login import TestLogin
# from test_add_to_cart import TestAddToCart

def suite():
    test_suite = unittest.TestSuite()

    # runTestNumber =  sys.argv[1] if len(sys.argv) > 1 else "all"
    # print(f"runTestNumber {runTestNumber}")

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
    
    # ECs: Testing of Cart Page
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCartPageUnitTest))
    
    # ECs: Testing of Cart Page
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestProfilePageUnitTest))
    
    # ECs: Testing of Cart Page
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test404RequestsUnitTest))

    # Integration Tests

    # ECs: Testing of add to cart integration
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddRemoveCartIntegrationTest))

    # ECs: Testing of book flight integration
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBookingIntegrationTest))

    # Security Tests

    # ECs: Testing of book flight by hacking session and user id
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSessionCloneSecurityTest))


    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddToCart))


    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())