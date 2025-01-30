from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginBeforeCheckout(BasePage):
   
    SIGNUP_LOGIN_LOCATOR = (By.LINK_TEXT, "Signup / Login")
    EMAIL_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]")
    PASSWORD_FEILD =(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]")  
    LOGIN_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
    LOGGED_IN_AS_TEXT = (By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a") 
    
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
    
    def login(self, email, password):
        self.click(self.SIGNUP_LOGIN_LOCATOR)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FEILD, password)
        self.click(self.LOGIN_BUTTON)

    def verify_logged_in(self):
        return self.is_element_visible(self.LOGGED_IN_AS_TEXT)

    def add_to_cart(self):
        self.click(self.PRODUCTS_BUTTON)
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
    
    def click_on_continue(self):
        self.click(self.CONTINUE_BUTTON1)