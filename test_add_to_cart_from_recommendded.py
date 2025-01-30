import time

import pytest
from config.config import Config
from pages.add_to_cart_from_recommendded_page import HomePage
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestHomePage:

    @pytest.mark.parametrize("url", [Config.BASE_URL])
    def test_recommended_items_in_cart(self, url):
        home_page = HomePage(self.driver)

        home_page.visit(url)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page successfully loaded.")

        home_page.verify_recommendded_item_section()
        print("'Recommended Items' section is visible.")

        home_page.click_on_add_to_cart()
        print("First recommended item added to cart.")

        home_page.click_on_view_cart()
        print("Clicked on 'View Cart' button.")

        home_page.verify_cart_products()
        print("Product is visible in the cart.")

        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="add_to_cart_recommendded"
        )
        print(f"Screenshot taken: {screenshot_path}")

        print("Test Case 22: for adding recommended product to cart passed.")
