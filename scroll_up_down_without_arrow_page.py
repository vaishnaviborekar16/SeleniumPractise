import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.scroll_helper import ScrollHelper


class ScrollWithoutArrowPage(BasePage):
    SUBSCRIPTION_SECTION = (By.XPATH, "//*[@id='footer']/div[1]/div/div/div[2]/div/h2")
    PRACTICE_WEBSITE_TEXT = (By.XPATH, "//*[contains(text(),'Full-Fledged practice website for Automation Engineers')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.scroll_helper = ScrollHelper(driver)

    def verify_subscription_visible(self):
        self.is_element_visible(self.SUBSCRIPTION_SECTION)
        time.sleep(2)

    def scroll_to_bottom(self):
        self.scroll_helper.scroll_to_bottom()

    def scroll_to_top(self):
        self.scroll_helper.scroll_to_top()

    def verify_practice_website_visible(self):
        self.is_element_visible(self.PRACTICE_WEBSITE_TEXT)
