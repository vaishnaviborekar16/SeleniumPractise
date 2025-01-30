import pytest
from config.config import Config
from pages.search_product_and_verify_cart_page import SearchCartPage
from utils.take_screenshot import take_screenshot

@pytest.mark.usefixtures("init_driver")
class TestSearchCart:
    @pytest.mark.parametrize("url, product_name, email, password", [
        (Config.BASE_URL, "Blue Top", "user2701@gmail.com", "user2701"),  # Pass email and password directly
    ])
    def test_search_cart(self, url, product_name, email, password):
        
        search_cart_page = SearchCartPage(self.driver)

        self.driver.get(url)
        self.driver.maximize_window()
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page loaded successfully.")

        
        search_cart_page.navigate_to_products_page()
        print("Navigated to Products page.")

        search_cart_page.search_for_product(product_name)
        assert search_cart_page.verify_search_results_visible(), "'Searched Products' not visible."
        print(f"Searched for '{product_name}' successfully.")

        search_cart_page.add_all_products_to_cart()
        print("All products added to the cart successfully.")

        search_cart_page.login(email, password)
        print("Logged in successfully.")
        search_cart_page.navigate_to_cart_page()
        search_cart_page.remove_all_products_from_cart()
        assert search_cart_page.is_cart_empty(), "'Cart is empty' message not visible."

        print("Verified cart is empty.")
        screenshot_path = take_screenshot(self.driver, "screenshots", "CartEmptyAfterSerchRemoval")
        print(f"Screenshot saved: {screenshot_path}")
        print("Test Case 20 : Serch and verify product in cart done..")
