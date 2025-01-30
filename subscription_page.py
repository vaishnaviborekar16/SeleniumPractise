from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.scroll_helper import ScrollHelper


class HomePage(BasePage):
    
    SUBSCRIPTION_TEXT = (By.XPATH, "//h2[text()='Subscription']")
    EMAIL_INPUT = (By.ID, "susbscribe_email")  
    SUBSCRIBE_BUTTON = (By.ID, "subscribe")  
    

    def __init__(self, driver):
        super().__init__(driver)
        self.scroll_helper = ScrollHelper(self.driver)  
    
    def scroll_to_footer(self):
        self.scroll_helper.scroll_to_bottom() 
    
    def enter_subscription_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)
    
    def click_subscribe(self):
        self.click(self.SUBSCRIBE_BUTTON)
    
    
