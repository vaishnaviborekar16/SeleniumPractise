import pytest
from pages.product_page import ProductsPage
from config.config import Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestProductsPage:
    @pytest.mark.parametrize(
        "url", [Config.BASE_URL]
    )
    def test_verify_all_products_and_product_details(self, url):
        products_page = ProductsPage(self.driver)
        products_page.visit(url)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page is successfully loaded.")

        products_page.navigate_to_products_page()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ProductsPage.ALL_PRODUCTS_HEADER)
        )
        assert products_page.is_products_page_visible(), "All Products page is not visible."
        print("All Products page is successfully loaded.")

        assert products_page.is_product_list_visible(), "Products list is not visible."
        print("Products list is visible.")

        products_page.click_view_first_product()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ProductsPage.PRODUCT_NAME)
        )
        print("Navigated to product detail page.")
        assert products_page.is_product_detail_visible(), "Product details are not visible."
        print("Product details are successfully verified.")
        
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="product_details"
        )
        print(f"Screenshot taken: {screenshot_path}")
        print("Test for All Products and Product Details page passed.")
