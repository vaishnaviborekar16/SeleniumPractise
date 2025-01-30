from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class RemoveProductFromCart(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    ADD_TO_CART_BUTTON = (By.XPATH, "(//a[text()='Add to cart'])[1]")
    VIEW_CART_BUTTON = (By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    REMOVE_PRODUCT_BUTTON = (By.XPATH, "//*[@id='product-1']/td[6]/a")
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[@id='empty_cart']/p/b")
    CART_ROWS = (By.XPATH, "//*[@id='cart_items']/tbody/tr")
    def go_to_products_page(self):
        self.click(self.PRODUCTS_BUTTON)

    def add_first_product_to_cart(self):
        self.driver.execute_script("window.scrollBy(0, 450)")
        self.click(self.ADD_TO_CART_BUTTON)

    def view_cart(self):
        self.click(self.VIEW_CART_BUTTON)

    def remove_product_from_cart(self):
        self.click(self.REMOVE_PRODUCT_BUTTON)

    def is_cart_empty(self):
        try:
            empty_cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMPTY_CART_MESSAGE)
         )
            return empty_cart.is_displayed()
        except:
            product_rows = self.driver.find_elements(self.CART_ROWS)
            return len(product_rows) == 0
