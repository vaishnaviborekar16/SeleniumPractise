from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    ALL_PRODUCTS_HEADER = (By.XPATH, "//h2[contains(text(), 'All Products')]")
    PRODUCT_LIST = (By.XPATH, "//div[@class='features_items']//div[@class='product-image-wrapper']")
    FIRST_PRODUCT_VIEW_BUTTON = (By.XPATH, "(//a[contains(text(), 'View Product')])[1]")
    PRODUCT_NAME = (By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2")
    PRODUCT_CATEGORY = (By.XPATH, "//p[contains(text(), 'Category:')]")
    PRODUCT_PRICE = (By.XPATH, "//span[contains(text(), 'Rs.')]")
    PRODUCT_AVAILABILITY = (By.XPATH, "//b[contains(text(), 'Availability:')]")
    PRODUCT_CONDITION = (By.XPATH, "//b[contains(text(), 'Condition:')]")
    PRODUCT_BRAND = (By.XPATH, "//b[contains(text(), 'Brand:')]")

    def navigate_to_products_page(self):
        self.click(self.PRODUCTS_BUTTON)
        print("Navigated to All Products page.")

    def is_products_page_visible(self):
        return self.find_web_element(self.ALL_PRODUCTS_HEADER)

    def is_product_list_visible(self):
        products = self.find_web_elements(self.PRODUCT_LIST)  
        print(f"Number of products visible: {len(products)}")
        return len(products) > 0

    def click_view_first_product(self):
        self.driver.execute_script("window.scrollBy(0, 450)")
        self.click(self.FIRST_PRODUCT_VIEW_BUTTON)
        print("Clicked on 'View Product' for the first product.")

    def is_product_detail_visible(self):
        detail_elements = {
            "Product Name": self.find_web_element(self.PRODUCT_NAME),
            "Category": self.find_web_element(self.PRODUCT_CATEGORY),
            "Price": self.find_web_element(self.PRODUCT_PRICE),
            "Availability": self.find_web_element(self.PRODUCT_AVAILABILITY),
            "Condition": self.find_web_element(self.PRODUCT_CONDITION),
            "Brand": self.find_web_element(self.PRODUCT_BRAND),
        }
        for key, element in detail_elements.items():
            print(f"{key} visible: {element is not None}")
        return all(element is not None for element in detail_elements.values())
