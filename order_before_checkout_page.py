from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TestPlaceOrderRegisterBeforeCheckout(BasePage):
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
    SIGNUP_NAME_FIELD = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL_FIELD = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
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
    
    ACCOUNT_CREATED_LABEL = (By.XPATH, "//*[@id='form']/div/div/div/h2/b")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div/div/a")
    LOGIN_USERNAME_LABEL = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
    
    PRODUCTS_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    ADD_TO_CART_BUTTON = (By.XPATH, "(//a[text()='Add to cart'])[1]")
    VIEW_CART_BUTTON = (By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//*[@id='do_action']/div[1]/div/div/a")
    ADD_COMMENTS =(By.XPATH, "//*[@id='ordermsg']/textarea")
    PLACE_ORDER_BUTTON = (By.XPATH, "//*[@id='cart_items']/div/div[7]/a")
    NANE_ON_CARD_FEILD= (By.XPATH,"//*[@id='payment-form']/div[1]/div/input")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@name='card_number']")
    CVC_FIELD = (By.XPATH, "//input[@name='cvc']")
    EXPIRATION_DATE_FIELD_MONTH = (By.XPATH, "//*[@id='payment-form']/div[3]/div[2]/input") 
    EXPIRATION_DATE_FIELD_YEAR = (By.XPATH, "//*[@id='payment-form']/div[3]/div[3]/input")
    PAY_AND_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Pay and Confirm Order']")
    ORDER_SUCCESS_LABEL = (By.XPATH, "//*[@id='form']/div/div/div/p")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]")
    ACCOUNT_DELETED_LABEL = (By.XPATH, "//*[@id='form']/div/div/div[1]/h2/b")
    CONTINUE_BUTTON1 = (By.XPATH, "//*[@id='form']/div/div/div/div/a")
    
    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_BUTTON)

    def fill_signup_form(self, name, email, password, day, month, year, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile):
        self.enter_text(self.SIGNUP_NAME_FIELD, name)
        self.enter_text(self.SIGNUP_EMAIL_FIELD, email)
        self.click(self.SIGNUP_BUTTON)
        self.click(self.TITLE_RADIO_BUTTON)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.select_option(self.DAY_DROPDOWN, day)
        self.select_option(self.MONTH_DROPDOWN, month)
        self.select_option(self.YEAR_DROPDOWN, year)
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.COMPANY, company)
        self.enter_text(self.ADDRESS1, address1)
        self.enter_text(self.ADDRESS2, address2)
        self.select_option(self.COUNTRY_DROPDOWN, country)
        self.enter_text(self.STATE, state)
        self.enter_text(self.CITY, city)
        self.enter_text(self.ZIPCODE, zipcode)
        self.enter_text(self.MOBILE_NUMBER, mobile)
        self.click(self.SUBMIT_BUTTON)

    def verify_account_created(self):
        return self.is_element_visible(self.ACCOUNT_CREATED_LABEL)

    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def view_cart(self):
        self.click(self.VIEW_CART_BUTTON)

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)

    def add_comments(self, comment_text):
        self.enter_text(self.ADD_COMMENTS, comment_text)

    def place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)

    def fill_payment_details(self, name_on_card, card_number, cvc, exp_month, exp_year):
        self.enter_text(self.NANE_ON_CARD_FEILD, name_on_card)
        self.enter_text(self.CARD_NUMBER_FIELD, card_number)
        self.enter_text(self.CVC_FIELD, cvc)
        self.enter_text(self.EXPIRATION_DATE_FIELD_MONTH, exp_month)
        self.enter_text(self.EXPIRATION_DATE_FIELD_YEAR, exp_year)
        self.click(self.PAY_AND_CONFIRM_BUTTON)

    def verify_order_success(self):
        return self.is_element_visible(self.ORDER_SUCCESS_LABEL)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_BUTTON)

    def verify_account_deleted(self):
        return self.is_element_visible(self.ACCOUNT_DELETED_LABEL)
    
    def click_continue_button1(self):
        self.click(self.CONTINUE_BUTTON1)
        