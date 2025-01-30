import time

import pytest
from config.config import Config
from pages.download_invoice_after_purchase_page import DownloadInvoice
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.scroll_helper import ScrollHelper
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestDownloadInvoiceFlow:
    def test_place_order_register_checkout(self):
        page = DownloadInvoice(self.driver)
        scroll_helper = ScrollHelper(self.driver)
        page.visit(Config.BASE_URL)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        page.click_products_button()

        page.driver.execute_script("window.scrollBy(0, 400)")

        page.add_to_cart()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(page.VIEW_CART_BUTTON)).click()
        page.proceed_to_checkout()
        page.click_register_login()
        page.fill_signup_details(
            name="John Dae",
            email="johndae245@gmail.com",
            password="password123",
            day="15",
            month="June",
            year="1990",
            first_name="John",
            last_name="Doe",
            company="Example Inc.",
            address1="12, Plm Street",
            address2="Apt 456",
            country="United States",
            state="California",
            city="Los Angeles",
            zipcode="90001",
            mobile="1234567890"
        )
        assert page.verify_account_created(), "Account creation failed."
        print("Account Created...!")
        page.click_continue_button()

        assert page.verify_login_username(), "User login verification failed."
        page.verify_cart_button()
        page.click_proceed_to_checkout_again()

        page.place_order()
        page.fill_payment_details(
            name_on_card="Test User",
            card_number="4111111111111111",
            cvc="123",
            exp_month="12",
            exp_year="2025"
        )

        assert page.verify_order_success(), "Order placement failed."
        print("Oreder palced successfully...!")
        
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="DownloadInvoice"
        )  
        page.download_invoice()
        print("Invoice donloded successfully...!")
      
        
        page.delete_account()
        assert page.verify_account_deleted(),"Account deletion failed."
        print("Account deleted successfully...!")
        
        
        print(f"Screenshot taken: {screenshot_path}")
        print("Test Case 24: Place Order: Download Invoice.")
        page.click_continue_button1()