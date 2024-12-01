import sys
import os


utils_path = os.path.abspath('tests')
utils_path_unit = os.path.abspath('tests/unit_tests')
sys.path.append(utils_path)
sys.path.append(utils_path_unit)

import unittest

from test_login_input import TestLoginInputUnitTest
from test_space_explorer_page import TestSpaceExplorerHeaderUnitTest
from test_launch_page import TestLauchPageUnitTest
from test_home_button import TestHomeButtonUnitTest
from test_cart_button import TestCartButtonUnitTest
from test_profile_button import TestProfileButtonUnitTest
from test_logout_button import TestLogoutButtonUnitTest
# from test_login import TestLogin
# from test_add_to_cart import TestAddToCart

def suite():
    test_suite = unittest.TestSuite()

    # EC1-3: Testing of Login Input Field
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLoginInputUnitTest))

    # EC4-7: Testing of Space Explorer Page
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSpaceExplorerHeaderUnitTest))
    
    # EC8-9: Testing of Launch Page
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLauchPageUnitTest))
    
    # EC10: Testing of Footer Button Home
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHomeButtonUnitTest))
    
    # EC11: Testing of Footer Button Home
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCartButtonUnitTest))
    
    # EC12: Testing of Footer Button Home
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestProfileButtonUnitTest))
    
    # EC13: Testing of Footer Button Home
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogoutButtonUnitTest))
    
    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddToCart))


    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())