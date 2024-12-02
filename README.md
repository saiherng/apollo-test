# apollo-test

Install Selenium

`$ pip install selenium`

Navigate to tests folder

`$ python test_suite.py`

# Tests List

## Unit Tests

- [EC1 PASS. Test Login input field with valid email address](./tests/unit_tests/test_login_input.py)
- [EC2 PASS. Test Login input field with invalid email address: String only](./tests/unit_tests/test_login_input.py)
- [EC3 PASS. Test Login input field with invalid email address: no domain](./tests/unit_tests/test_login_input.py)
- [EC4 PASS. Test Login button](./tests/unit_tests/test_login_button.py)
- [EC5 PASS. Test Home Page Exists](./tests/unit_tests/test_home_page.py)
- [EC6 PASS. Test Home Page is not accessible without signin](./tests/unit_tests/test_home_page.py)
- [EC7 PASS. Test that the header shows the correct email address](./tests/unit_tests/test_home_page.py)
- [EC8 PASS. Test that the page loads a list of 1 or more flights](./tests/unit_tests/test_home_page.py)
- [EC9 PASS. Test that flight list paginates, and tests adds more button](./tests/unit_tests/test_home_page.py)
- [EC10 PASS. Test that the flight link goes to flight page](./tests/unit_tests/test_home_page.py)
- [EC11 PASS. Test that the page exists and content loaded](./tests/unit_tests/test_launch_page.py)
- [EC12 PASS. Test Launch Page is not accessible without signin](./tests/unit_tests/test_launch_page.py)
- [EC13 PASS. Test Add To Cart Button Texts](./tests/unit_tests/test_launch_page.py)
- [EC14 PASS. Test non existing launch id while signed in](./tests/unit_tests/test_launch_page.py)
- [EC15 PASS. Test non given launch id while signed in](./tests/unit_tests/test_launch_page.py)
- [EC16 PASS. Test Home Button Navigation](./tests/unit_tests/test_home_button.py)
- [EC17 PASS. Test Cart Button Navigation](./tests/unit_tests/test_cart_button.py)
- [EC18 PASS. Test Profile Button Navigation](./tests/unit_tests/test_profile_button.py)
- [EC19 PASS. Test Logout Button Navigation](./tests/unit_tests/test_logout_button.py)
- [EC20 PASS. Test Cart Page Exists](./tests/unit_tests/test_cart_page.py)
- [EC21 PASS. Test Cart Page is not accessible without signin](./tests/unit_tests/test_cart_page.py)
- [EC22 PASS. Test Profile Page Exists](./tests/unit_tests/test_profile_page.py)
- [EC23 PASS. Test Profile Page is not accessible without signin](./tests/unit_tests/test_profile_page.py)
- [EC24 PASS. Test non existing page while signed in](./tests/unit_tests/test_404_requests.py)
- [EC25 PASS. Test non existing page while signed out](./tests/unit_tests/test_404_requests.py)

## Integration Tests

- [EC26 PASS. Test Add To Cart Button Action](./tests/integration_tests/test_add_remove_cart.py)
- [EC27 PASS. Test Remove From Cart Button Action](./tests/integration_tests/test_add_remove_cart.py)
- [EC28 PASS. Test Book One Flight](./tests/integration_tests/test_add_remove_cart.py)
- [EC29 PASS. Test Book Two Flights](./tests/integration_tests/test_add_remove_cart.py)
- [EC30 PASS. Test Remove booked flight](./tests/integration_tests/test_add_remove_cart.py)
- [EC31 PASS. Test Remove all booked flights](./tests/integration_tests/test_add_remove_cart.py)

