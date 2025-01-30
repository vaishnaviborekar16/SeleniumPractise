from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    FIRST_PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[1]")
    ADD_TO_CART_BUTTON_1 = (By.XPATH, "(//a[text()='Add to cart'])[1]")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//*[@id='cartModal']/div/div/div[3]/button")
    SECOND_PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[2]")
    ADD_TO_CART_BUTTON_2 = (By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
    VIEW_CART_BUTTON = (By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    CART_PRODUCTS = (By.XPATH, "//*[@id='cart_info_table']/thead/tr/td[1]")
    CART_ROW = (By.XPATH, "//*[@id='cart_info_table']//tbody/tr")

    def click_products_button(self):
        self.click(self.PRODUCTS_BUTTON)
    
    def hover_and_add_to_cart(self, product_index):
        product = self.FIRST_PRODUCT if product_index == 1 else self.SECOND_PRODUCT
        add_to_cart_button = self.ADD_TO_CART_BUTTON_1 if product_index == 1 else self.ADD_TO_CART_BUTTON_2
        
        product_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(product)
        )
        add_to_cart_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(add_to_cart_button)
        )
        action = ActionChains(self.driver)
        action.move_to_element(product_element).click(add_to_cart_button_element).perform()
    
    def click_continue_shopping(self):
        continue_shopping_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
        )
        continue_shopping_button.click()
    
    def click_view_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.VIEW_CART_BUTTON)
        )
        self.click(self.VIEW_CART_BUTTON)
    
    def get_cart_products(self):
        return self.driver.find_elements(*self.CART_ROW)    
    
    