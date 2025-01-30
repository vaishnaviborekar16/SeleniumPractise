import pytest
from config.config import Config
from pages.login_with_incorrect_credintials_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.data_provider import DataProvider
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestLoginIncorrect:

    def test_login_with_incorrect_credentials(self):

        login_page = LoginPage(self.driver)
        login_page.visit(Config.BASE_URL)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPage.SIGNUP_LOGIN_LOCATOR)
        )
        login_page.login(email="user27011@gmail.com", password="user2701555")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPage.ERROR_MESSAGE)
        )
        assert login_page.verify_login_error_message(), (
            "Error message not displayed or incorrect for invalid login."
        )
        print("Login failed as expected: Invalid credentials.")

        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="login_error"
        )
        print(f"Screenshot taken: {screenshot_path}")
