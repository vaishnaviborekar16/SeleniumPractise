import pytest
from config.config import Config
from pages.remove_product_from_cart_page import RemoveProductFromCart
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestRemoveProductFromCart:
    def test_remove_product_from_cart(self):
        remove_product_page = RemoveProductFromCart(self.driver)

        self.driver.get(Config.BASE_URL)
        remove_product_page.go_to_products_page()
        remove_product_page.add_first_product_to_cart()
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(remove_product_page.VIEW_CART_BUTTON)).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(remove_product_page.REMOVE_PRODUCT_BUTTON)).click()

        assert remove_product_page.is_cart_empty(), "The cart is not empty after removing the product."

        screenshot_path = take_screenshot(self.driver, "screenshots", "CartEmptyAfterProductRemoval")
        print(f"Screenshot saved at: {screenshot_path}")
        print("Test Case 17: Remove Product from Cart - Passed!")
