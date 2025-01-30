import pytest
from config.config import Config
from pages.search_product_page import HomePage
from utils.scroll_helper import ScrollHelper
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestSearchProduct:

    @pytest.mark.parametrize("url, product_name", [
        (Config.BASE_URL, "Blue Top"),  
    ])
    def test_search_product(self, url, product_name):
        home_page = HomePage(self.driver)
        scroll_helper = ScrollHelper(self.driver) 
        home_page.visit(url)
        
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page is successfully loaded.")

        home_page.click_products_button()
        print("Navigated to Products page.")

        assert "All Products" in self.driver.page_source, "All Products page is not visible."
        print("Verified All Products page is visible.")

        home_page.search_product(product_name)
        print(f"Search for product '{product_name}' performed.")

        searched_products = home_page.get_searched_products()  
        if searched_products:
            first_product = searched_products[0] 
            scroll_helper.scroll_to_element_and_center(first_product)  
            print(f"Scrolled to the first product '{product_name}' to center.")

        assert home_page.verify_searched_products_visible(), "'Searched Products' label is not visible."
        print("'Searched Products' is visible.")

        assert len(searched_products) > 0, f"No products found for the search '{product_name}'."
        print(f"Number of products found for '{product_name}': {len(searched_products)}")

        screenshot_path = take_screenshot(self.driver, "screenshots", f"searched_products_{product_name.replace(' ', '_')}")
        print(f"Screenshot of searched products taken: {screenshot_path}")        
