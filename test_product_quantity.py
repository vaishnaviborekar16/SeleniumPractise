import pytest
from config.config import Config
from pages.verify_product_quantity_page import ProductDetailPage
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestVerifyProductQuantityInCart:
    
    @pytest.mark.parametrize("url", [Config.BASE_URL])
    def test_product_quantity_in_cart(self, url):
        product_page = ProductDetailPage(self.driver)
        product_page.visit(url)
        
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page is successfully loaded.")
        
        product_page.click_view_product()
        print("Navigated to Product Detail page.")
        
        assert "Product Detail" in self.driver.page_source, "Product detail page is not visible."
        print("Product detail page is visible.")
        product_page.increase_quantity(4)
        print("Increased product quantity to 4.")
        product_page.click_add_to_cart()
        print("Product added to the cart.")
        
        product_page.click_view_cart()
        print("Navigated to View Cart page.")
        
        cart_quantity = product_page.get_cart_product_quantity()
        assert cart_quantity == "4", f"Expected quantity '4' but got {cart_quantity}."
        print(f"Product quantity in the cart is correctly set to {cart_quantity}.")
        
        screenshot_path = take_screenshot(self.driver, "screenshots", "incersing_product_quantity")
        print(f"Screenshot taken: {screenshot_path}")
        
        print("Test for product quantity in cart passed.")
