import pytest
from config.config import Config
from pages.logout_page import LogoutPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.data_provider import DataProvider
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestLogout:

    def test_logout_user(self):
       
        login_page = LogoutPage(self.driver)

        
        login_page.visit(Config.BASE_URL)

        assert self.driver.title == "Automation Exercise", "Home page not visible successfully!"

        login_page.click(LogoutPage.SIGNUP_LOGIN_LOCATOR)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutPage.LOGIN_PAGE_HEADER)
        )
        assert login_page.verify_login_page(), "'Login to your account' is not visible!"

        login_page.login(email="user2701@gmail.com", password="user2701")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutPage.LOGGED_IN_AS_TEXT)
        )
        assert login_page.verify_logged_in(), "'Logged in as username' is not visible!"

        login_page.logout()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutPage.LOGIN_PAGE_HEADER)
        )
        assert login_page.verify_login_page(), "User was not navigated back to the login page after logout!"
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="logout_user_success"
        )
        print(f"Screenshot taken: {screenshot_path}")
