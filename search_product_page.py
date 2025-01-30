from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_LABEL = (By.XPATH, "//h2[text()='Searched Products']")
    PRODUCT_LIST = (By.XPATH, "//div[@class='product-overlay']")

    def click_products_button(self):
        self.click(self.PRODUCTS_BUTTON)

    def search_product(self, product_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SEARCH_INPUT)).send_keys(product_name)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def verify_searched_products_visible(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SEARCHED_PRODUCTS_LABEL)).is_displayed()

    def get_searched_products(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.PRODUCT_LIST))
