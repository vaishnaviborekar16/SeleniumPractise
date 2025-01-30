import pytest
from config.config import Config
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.data_provider import DataProvider
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.visit(Config.BASE_URL)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPage.SIGNUP_LOGIN_LOCATOR)
        )

        login_page.login(email="user2701@gmail.com", password="user2701")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginPage.LOGGED_IN_AS_TEXT)
            )
            assert login_page.verify_logged_in(), "Login verification failed! 'Logged in as' text is not visible."
            print("Login successful!")
        except Exception as e:
            print(f"Error verifying login: {e}")
            raise
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="login_success"
        )
        print(f"Screenshot taken: {screenshot_path}")
