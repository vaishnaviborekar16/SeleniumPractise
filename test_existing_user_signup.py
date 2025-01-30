import pytest
from config.config import Config
from pages.existing_user_signup_page import SignupPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.data_provider import DataProvider
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestRegisterExistingEmail:

    def test_register_with_existing_email(self):
        signup_page = SignupPage(self.driver)
        signup_page.visit(Config.BASE_URL)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SignupPage.SIGNUP_LOCATOR)
        )
        signup_page.click(SignupPage.SIGNUP_LOCATOR)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(SignupPage.NAME_FIELD)
        )

        email="user2701@gmail.com"
        signup_page.signup(name="user2701", email=email)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SignupPage.EMAIL_EXISTS_ERROR_MESSAGE)
        )

        assert signup_page.verify_text_visible(SignupPage.EMAIL_EXISTS_ERROR_MESSAGE), (
            "Error message for existing email is not displayed or incorrect."
        )
        print(f"Signup failed as expected: Email '{email}' already exists.")
        
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="signup_error"
        )
        print(f"Screenshot taken: {screenshot_path}")
