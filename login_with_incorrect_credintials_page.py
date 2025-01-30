from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    SIGNUP_LOGIN_LOCATOR = (By.LINK_TEXT, "Signup / Login")
    EMAIL_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")  
    ERROR_MESSAGE = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/p")  

    def login(self, email, password):
        self.click(self.SIGNUP_LOGIN_LOCATOR)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        print("Login attempted with provided credentials.")

    def verify_login_error_message(self):
        try:
            element = self.find_web_element(self.ERROR_MESSAGE)
            return element.is_displayed() and "Your email or password is incorrect!" in element.text
        except Exception as e:
            print(f"Error in verifying login error message: {e}")
            return False
