from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def visit(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        
    def find_web_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_web_elements(self, locator, timeout=10):
       
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def enter_text(self, locator, text):
        element = self.find_web_element(locator)
        element.send_keys(text)
    
    def click(self, locator):
        element = self.find_web_element(locator)
        element.click()
        
    def select_option(self, locator, option_text):
        dropdown_element = self.find_web_element(locator)
       
        select = Select(dropdown_element)
       
        select.select_by_visible_text(option_text)
        
    def is_element_visible(self, locator):
        try:
            return self.find_web_element(locator).is_displayed()
        except:
            return False    
