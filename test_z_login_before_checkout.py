import pytest
from config.config import Config
from pages.login_before_checkout_page import LoginBeforeCheckout
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestLoginBeforeCheckout:
    def test_login_and_place_order(self):
        page = LoginBeforeCheckout(self.driver)
        page.visit(Config.BASE_URL)

        assert "Automation Exercise" in self.driver.title, "Home page title does not match."

        page.login(email="user2701@gmail.com", password="user2701")
        assert page.verify_logged_in(), "Login failed or logged-in text not visible."
        
        page.add_to_cart()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(page.VIEW_CART_BUTTON)).click()
        assert page.is_element_visible(page.PROCEED_TO_CHECKOUT_BUTTON), "Checkout button not visible."
        page.proceed_to_checkout()
        page.add_comments("Place Order!")
        page.place_order()
        page.fill_payment_details(
            name_on_card="ALex Peter",
            card_number="9765476890",
            cvc="123",
            exp_month="12",
            exp_year="2025"
        )
        assert page.verify_order_success(), "Order confirmation failed."
        page.delete_account()
        assert page.verify_account_deleted(), "Account deletion failed."

        screenshot_path = take_screenshot(self.driver, "screenshots", "OrderPlacedLoginBeforeCheckout")
        print(f"Screenshot saved: {screenshot_path}")
        print("Test Case 16: Login Before Checkout - Passed!")
        page.click_on_continue()
