import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactUsPage(BasePage):
    CONTACT_US_BUTTON = (By.LINK_TEXT, "Contact us")
    GET_IN_TOUCH_TEXT = (By.XPATH, "//*[@id='contact-page']/div[2]/div[1]/div/h2")
    NAME_FIELD = (By.XPATH, "//*[@id='contact-us-form']/div[1]/input")
    EMAIL_FIELD = (By.XPATH, "//*[@id='contact-us-form']/div[2]/input")
    SUBJECT_FIELD = (By.XPATH, "//*[@id='contact-us-form']/div[3]/input")
    MESSAGE_FIELD = (By.XPATH, "//*[@id='contact-us-form']/div[4]/textarea")
    UPLOAD_FILE_BUTTON = (By.XPATH, "//*[@id='contact-us-form']/div[5]/input")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='contact-us-form']/div[6]/input")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Success! Your details have been submitted successfully.')]")
    HOME_BUTTON = (By.XPATH, "//*[@id='form-section']/a/span")

    def fill_contact_form(self, name, email, subject, message, file_path):
        self.enter_text(self.NAME_FIELD, name)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.SUBJECT_FIELD, subject)
        self.enter_text(self.MESSAGE_FIELD, message)
        self.driver.execute_script("window.scrollBy(0, 100)")
        time.sleep(1)
        self.find_web_element(self.UPLOAD_FILE_BUTTON).send_keys(file_path)
        self.click(self.SUBMIT_BUTTON)
        print("Contact form submitted.")

    def verify_success_message(self):
        return self.find_web_element(self.SUCCESS_MESSAGE)

    def click_home_button(self):
        self.click(self.HOME_BUTTON)
        print("Navigated back to the home page.")
