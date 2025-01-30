import pytest
from config.config import Config
from pages.user_registraion_page import RegisterUserPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.data_provider import DataProvider
from utils.scroll_helper import ScrollHelper
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestRegisterUser:

    def test_register_user(self):
        register_page = RegisterUserPage(self.driver)
        scroll_helper = ScrollHelper(self.driver)
        register_page.visit(Config.BASE_URL)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegisterUserPage.SIGNUP_LOGIN_LOCATOR)
        )
        register_page.click(RegisterUserPage.SIGNUP_LOGIN_LOCATOR)

        register_page.signup(name="user2701", email="user2701@gmail.com")

        scroll_helper.scroll_to_bottom()

        register_page.register_user_details(
            password="user2701",
            day="15",
            month="May",
            year="1999",
            first_name="User",
            last_name="29011900",
            company="Pie Tech",
            address1="Palm Street",
            address2="Bella casa Apt",
            country="India",
            state="MH",
            city="Pune",
            zipcode="457458",
            mobile="9595248712"
        )

        scroll_helper.scroll_to_top()

        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h2"), "ACCOUNT CREATED!")
        )
        success_message = self.driver.find_element(By.TAG_NAME, "h2").text
        assert success_message == "ACCOUNT CREATED!", f"Expected 'ACCOUNT CREATED!', but got '{success_message}'"
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="register_user_success"
        )
        print(f"Screenshot taken: {screenshot_path}")
