import pytest
from config.config import Config
from pages.verify_address_details_in_checkout_page import TestAdressBeforeCheckout
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestPlaceOrderRegisterBeforeCheckoutFlow:
    def test_place_order_register_before_checkout(self):
        page = TestAdressBeforeCheckout(self.driver)
        page.visit(Config.BASE_URL)

        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        page.click_signup_login()
        page.fill_signup_form(
            name="Jane Doe",
            email="janedoe831@gmail.com",
            password="test1234",
            day="10",
            month="January",
            year="1995",
            first_name="Jane",
            last_name="Doe",
            company="TestCorp",
            address1="123 Testing Blvd",
            address2="Suite 100",
            country="United States",
            state="New York",
            city="New York City",
            zipcode="10001",
            mobile="9876543210"
        )
        assert page.verify_account_created(), "Account creation failed."
        page.click_continue_button()

        assert page.is_element_visible(page.LOGIN_USERNAME_LABEL), "Logged in username not visible."

        page.click(page.PRODUCTS_BUTTON)
        page.add_to_cart()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(page.VIEW_CART_BUTTON)).click()
        
        assert page.is_element_visible(page.PROCEED_TO_CHECKOUT_BUTTON), "Checkout button not visible."
        page.proceed_to_checkout()
        
        screenshot_path = take_screenshot(self.driver, "screenshots", "VerifyAdressBeforeCheckout")
        print(f"Screenshot saved: {screenshot_path}")
        
        
        page.delete_account()
        assert page.verify_account_deleted(), "Account deletion failed."

       
        print("Test Case 23: Place Order: Verify Address Before Checkout - Passed!")
        page.click_continue_button1()