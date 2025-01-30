from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):
    SIGNUP_LOCATOR = (By.LINK_TEXT, "Signup / Login")
    NAME_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[2]")
    EMAIL_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]")
    SIGNUP_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button")
    EMAIL_EXISTS_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Email Address already exist!')]")

    def signup(self, name, email):
        self.enter_text(self.NAME_FIELD, name)
        self.enter_text(self.EMAIL_FIELD, email)
        self.click(self.SIGNUP_BUTTON)
        print(f"Signup attempted with email: {email}")

    def verify_email_exists_error(self):
        try:
            element = self.find_web_element(self.EMAIL_EXISTS_ERROR_MESSAGE)
            return element.is_displayed() and "Email Address already exist!" in element.text
        except Exception as e:
            print(f"Error verifying email exists message: {e}")
            return False

    def verify_text_visible(self, locator):
        try:
            element = self.find_web_element(locator)
            return element.is_displayed()
        except Exception as e:
            print(f"Error in verifying text visibility: {e}")
            return False
