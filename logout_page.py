from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoutPage(BasePage):
    SIGNUP_LOGIN_LOCATOR = (By.LINK_TEXT, "Signup / Login")
    EMAIL_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
    LOGGED_IN_AS_TEXT = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    LOGIN_PAGE_HEADER = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/h2")  

    def login(self, email, password):
        self.click(self.SIGNUP_LOGIN_LOCATOR)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        print("Login completed...!")

    def verify_logged_in(self):
        try:
            element = self.find_web_element(self.LOGGED_IN_AS_TEXT)
            return element.is_displayed()
        except Exception as e:
            print(f"Error in verifying login: {e}")
            return False

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
        print("Logout completed...!")

    def verify_login_page(self):
        try:
            element = self.find_web_element(self.LOGIN_PAGE_HEADER)
            return element.is_displayed()
        except Exception as e:
            print(f"Error in verifying login page: {e}")
            return False
