import time

import pytest
from config.config import Config
from pages.contact_us_page import ContactUsPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.data_provider import DataProvider
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestContactUsForm:

    def test_contact_us_form(self):
        contact_us_page = ContactUsPage(self.driver)


        contact_us_page.visit(Config.BASE_URL)

        assert "Automation Exercise" in self.driver.title, "Home page title does not match."

        contact_us_page.click(ContactUsPage.CONTACT_US_BUTTON)
        
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ContactUsPage.GET_IN_TOUCH_TEXT)
        )
        assert contact_us_page.find_web_element(ContactUsPage.GET_IN_TOUCH_TEXT), (
            "'GET IN TOUCH' text is not visible."
        )

        contact_us_page.fill_contact_form(
            name="Vaishnavi",
            email="vaishnavi@gmail.com",
            subject="test",
            message="test",
            file_path="C://Users//asus//PycharmProjects//Capstone_project//file.txt",
        )
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        print("Alert accepted after form submission.")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ContactUsPage.SUCCESS_MESSAGE)
        )
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="contact_us"
        )
        print(f"Screenshot taken: {screenshot_path}")

        assert contact_us_page.verify_success_message(), (
            "Success message for contact form submission is not visible."
        )
        contact_us_page.click_home_button()

        assert "Automation Exercise" in self.driver.title, (
            "Failed to navigate back to the home page."
        )
        print(f"Test case for contact us form with kunal passed.")

    