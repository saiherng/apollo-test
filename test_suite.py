import sys
import os


utils_path = os.path.abspath('tests')
sys.path.append(utils_path)

import unittest

from test_login import TestLogin
from test_add_to_cart import TestAddToCart

def suite():
    test_suite = unittest.TestSuite()
    
    #test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddToCart))


    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())