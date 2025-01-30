from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.scroll_helper import ScrollHelper


class HomePage(BasePage):
    SUBSCRIPTION_SECTION = (By.XPATH, "//*[@id='footer']/div[1]/div/div/div[2]/div/h2")
    SCROLL_UP_ARROW = (By.XPATH, "//i[@class='fa fa-angle-up']")
    PRACTICE_WEBSITE_TEXT = (By.XPATH, "//*[contains(text(),'Full-Fledged practice website for Automation Engineers')]")
    
    def __init__(self, driver):
        super().__init__(driver) 
        self.scroll_helper = ScrollHelper(driver)  

    def verify_subscription_visible(self):
        self.is_element_visible(self.SUBSCRIPTION_SECTION)

    def scroll_to_bottom(self):
        self.scroll_helper.scroll_to_bottom()

    def click_scroll_up_arrow(self):
        scroll_up_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SCROLL_UP_ARROW)
        )
        scroll_up_button.click()

    def verify_practice_website_visible(self):
        self.is_element_visible(self.PRACTICE_WEBSITE_TEXT)

