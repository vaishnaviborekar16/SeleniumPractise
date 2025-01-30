from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegisterUserPage(BasePage):
    SIGNUP_LOGIN_LOCATOR = (By.LINK_TEXT, "Signup / Login")
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]") 
    SIGNUP_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button") 
    TITLE_RADIO_BUTTON = (By.ID, "id_gender2")  
    PASSWORD_FIELD = (By.ID, "password")
    DAY_DROPDOWN = (By.ID, "days")
    MONTH_DROPDOWN = (By.ID, "months")
    YEAR_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Create Account')]")

    def signup(self, name, email):
        self.enter_text(self.NAME_FIELD, name)
        self.enter_text(self.EMAIL_FIELD, email)
        self.click(self.SIGNUP_BUTTON)

    def register_user_details(self, password, day, month, year, first_name, last_name,
                              company, address1, address2, country, state, city, zipcode, mobile):
        self.click(self.TITLE_RADIO_BUTTON)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.select_dropdown(self.DAY_DROPDOWN, day)
        self.select_dropdown(self.MONTH_DROPDOWN, month)
        self.select_dropdown(self.YEAR_DROPDOWN, year)
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.OFFERS_CHECKBOX)
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.COMPANY, company)
        self.enter_text(self.ADDRESS1, address1)
        self.enter_text(self.ADDRESS2, address2)
        self.select_dropdown(self.COUNTRY_DROPDOWN, country)
        self.enter_text(self.STATE, state)
        self.enter_text(self.CITY, city)
        self.enter_text(self.ZIPCODE, zipcode)
        self.enter_text(self.MOBILE_NUMBER, mobile)
        self.click(self.SUBMIT_BUTTON)
        print("Registraion Completed...!")

    def select_dropdown(self, locator, value):
        dropdown = Select(self.find_web_element(locator))
        try:
            dropdown.select_by_value(value)  
        except Exception:
            dropdown.select_by_visible_text(value)  