import sys
import os


utils_path = os.path.abspath('tests')
utils_path_unit = os.path.abspath('tests/unit_tests')
sys.path.append(utils_path)
sys.path.append(utils_path_unit)

import unittest

from test_login_input import TestLoginInputUnitTest
# from test_login import TestLogin
# from test_add_to_cart import TestAddToCart

def suite():
    test_suite = unittest.TestSuite()

    # EC1-3: Testing of Login Input Field
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLoginInputUnitTest))
    
    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddToCart))


    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())