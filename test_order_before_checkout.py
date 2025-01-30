import pytest
from config.config import Config
from pages.order_before_checkout_page import TestPlaceOrderRegisterBeforeCheckout
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestPlaceOrderRegisterBeforeCheckoutFlow:
    def test_place_order_register_before_checkout(self):
        page = TestPlaceOrderRegisterBeforeCheckout(self.driver)
        page.visit(Config.BASE_URL)

        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        page.click_signup_login()
        page.fill_signup_form(
            name="Jane Doe",
            email="janedoe343@gmail.com",
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

        page.add_comments("'Place Order.")
        page.place_order()

        page.fill_payment_details(
            name_on_card="Jane Doe",
            card_number="4234567889",
            cvc="123",
            exp_month="12",
            exp_year="2025"
        )

        assert page.verify_order_success(), "Order confirmation failed."

        page.delete_account()
        assert page.verify_account_deleted(), "Account deletion failed."

        screenshot_path = take_screenshot(self.driver, "screenshots", "OrderPlacedBeforeCheckout")
        print(f"Screenshot saved: {screenshot_path}")
        print("Test Case 15: Place Order: Register Before Checkout - Passed!")
        page.click_continue_button1()