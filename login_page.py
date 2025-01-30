from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    SIGNUP_LOGIN_LOCATOR = (By.LINK_TEXT, "Signup / Login")
    EMAIL_FIELD = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]")
    PASSWORD_FEILD =(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]")  
    LOGIN_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
    LOGGED_IN_AS_TEXT = (By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a") 
   
    def login(self,email,password):
        self.click(self.SIGNUP_LOGIN_LOCATOR)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FEILD,password)
        self.click(self.LOGIN_BUTTON)
        
    
    def verify_logged_in(self):
        try:
            element=self.find_web_element(self.LOGGED_IN_AS_TEXT)
            return element.is_displayed()
        except:
            return False    
        
        