import pytest
from config.config import Config
from pages.add_product_cart_page import HomePage
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestAddProductsToCart:
    
    @pytest.mark.parametrize("url", [Config.BASE_URL])
    def test_add_products_in_cart(self, url):
        home_page = HomePage(self.driver)
        home_page.visit(url)
    
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page is successfully loaded.")
        
        home_page.click_products_button()
        print("Navigated to Products page.")
        
        home_page.hover_and_add_to_cart(1)
        print("First product added to cart.")
        
        home_page.click_continue_shopping()
        print("Clicked 'Continue Shopping'.")
        
        home_page.hover_and_add_to_cart(2)
        print("Second product added to cart.")
        
        home_page.click_view_cart()
        print("Navigated to View Cart page.")
        
        cart_products = home_page.get_cart_products()
        assert len(cart_products) == 2, "Both products are not in the cart."
        print(f"Number of products in cart: {len(cart_products)}")
        

        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="adding_products_to_cart"
        )
        print(f"Screenshot taken: {screenshot_path}")
        