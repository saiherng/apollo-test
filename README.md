# apollo-test

Install Selenium

`$ pip install selenium`

Navigate to tests folder

`$ python test_suite.py`

# Tests List

## Unit Tests

- [EC1: Test Login input field with valid email address](./tests/unit_tests/test_login_input.py)
- [EC2: Test Login input field with invalid email address: String only](./tests/unit_tests/test_login_input.py)
- [EC3: Test Login input field with invalid email address: no domain](./tests/unit_tests/test_login_input.py)
- [EC4: Test Login button](./tests/unit_tests/test_login_button.py)
- [EC5: Test Home Page Exists](./tests/unit_tests/test_home_page.py)
- [EC6: Test Home Page is not accessible without signin](./tests/unit_tests/test_home_page.py)
- [EC7: Test that the header shows the correct email address](./tests/unit_tests/test_home_page.py)
- [EC8: Test that the page loads a list of 1 or more flights](./tests/unit_tests/test_home_page.py)
- [EC9: Test that flight list paginates, and tests adds more button](./tests/unit_tests/test_home_page.py)
- [EC10: Test that the flight link goes to flight page](./tests/unit_tests/test_home_page.py)
- [EC11: Test that the page exists and content loaded](./tests/unit_tests/test_launch_page.py)
- [EC12: Test Launch Page is not accessible without signin](./tests/unit_tests/test_launch_page.py)
- [EC13: Test Add To Cart Button Texts](./tests/unit_tests/test_launch_page.py)
- [EC14: Test non existing launch id while signed in](./tests/unit_tests/test_launch_page.py)
- [EC15: Test non given launch id while signed in](./tests/unit_tests/test_launch_page.py)
- [EC16: Test Home Button Navigation](./tests/unit_tests/test_home_button.py)
- [EC17: Test Cart Button Navigation](./tests/unit_tests/test_cart_button.py)
- [EC18: Test Profile Button Navigation](./tests/unit_tests/test_profile_button.py)
- [EC19: Test Logout Button Navigation](./tests/unit_tests/test_logout_button.py)
- [EC20: Test Cart Page Exists](./tests/unit_tests/test_cart_page.py)
- [EC21: Test Cart Page is not accessible without signin](./tests/unit_tests/test_cart_page.py)
- [EC22: Test Profile Page Exists](./tests/unit_tests/test_profile_page.py)
- [EC23: Test Profile Page is not accessible without signin](./tests/unit_tests/test_profile_page.py)
- [EC24: Test non existing page while signed in](./tests/unit_tests/test_404_requests.py)
- [EC25: Test non existing page while signed out](./tests/unit_tests/test_404_requests.py)

## Integration Tests

- [EC26: Test Add To Cart Button Action](./tests/integration_tests/test_add_remove_cart.py)
- [EC27: Test Remove From Cart Button Action](./tests/integration_tests/test_add_remove_cart.py)
- [EC28: Test Book One Flight](./tests/integration_tests/test_add_remove_cart.py)
- [EC29: Test Book Two Flights](./tests/integration_tests/test_add_remove_cart.py)

## System Tests
- [EC30: Test Remove booked flight](./tests/system_tests/test_add_remove_cart.py)
- [EC31: Test Remove all booked flights](./tests/system_tests/test_add_remove_cart.py)

## Security Tests
- [EC32: Test loging with stolen token](./tests/security_tests/test_session_clone.py)
- [EC33: Test login field against sql injection](./tests/security_tests/test_sql_injection.py)
- [EC34: Test flights url against sql injection](./tests/security_tests/test_sql_injection.py)