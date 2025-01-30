from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(BasePage):
    HOME_PAGE_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[1]/a")
    RECOMMENDED_ITEMS_SECTION = (By.XPATH, "//h2[contains(text(), 'Recommended Items')]")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//*[@id='recommended-item-carousel']/div/div[1]/div[1]/div/div/div/a")
    VIEW_CART_BUTTON = (By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    CART_PRODUCT = (By.XPATH, "//*[@id='product-1']")

    
    def verify_recommendded_item_section(self):
        self.is_element_visible(self.RECOMMENDED_ITEMS_SECTION)
    
    def click_on_add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.ADD_TO_CART_BUTTONS)
        )
        self.click(self.ADD_TO_CART_BUTTONS)
   
    def click_on_view_cart(self):
        view_cart_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.VIEW_CART_BUTTON) 
        )
        view_cart_button.click()

        
    def verify_cart_products(self):
        self.is_element_visible(self.CART_PRODUCT)    
        
          