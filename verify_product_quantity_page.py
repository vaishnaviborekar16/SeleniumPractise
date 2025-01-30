import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductDetailPage(BasePage):
    VIEW_PRODUCT_BUTTON = (By.XPATH, "(//a[text()='View Product'])[1]") 
    QUANTITY_INPUT = (By.XPATH, "//input[@id='quantity']")
    ADD_TO_CART_BUTTON = (By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
    VIEW_CART_BUTTON = (By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    CART_PRODUCT_QUANTITY = (By.XPATH, "//*[@id='cart_info_table']/tbody/tr/td[4]") 
    
    def click_view_product(self):
        self.driver.execute_script("window.scrollBy(0, 600)")
        self.click(self.VIEW_PRODUCT_BUTTON)

    def increase_quantity(self, quantity):
        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.QUANTITY_INPUT)
        )
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))  

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
    
    def click_view_cart(self):
      cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.VIEW_CART_BUTTON)
        )
      self.click(self.VIEW_CART_BUTTON)

    def get_cart_product_quantity(self):
        return self.driver.find_element(*self.CART_PRODUCT_QUANTITY).text
