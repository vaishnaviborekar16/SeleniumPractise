import pytest
from config.config import Config
from pages.view_brand_products_page import BrandPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestBrandProducts:
    def test_view_brand_products(self):
        brand_page = BrandPage(self.driver)

        self.driver.get(Config.BASE_URL)
        self.driver.maximize_window()

        assert brand_page.verify_brands_visible(), "Brands are not visible in the left sidebar."

        brand_page.click_brand_1()

        brand_page.click_brand_2()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(brand_page.BRAND_PAGE_HEADER)
        )
        assert brand_page.verify_brand_page_header(), "Brand 2 page is not displayed."

        screenshot_path = take_screenshot(self.driver, "screenshots", "Brand2Page")
        print(f"Screenshot saved at: {screenshot_path}")

        print("Verified Brand 2 product page successfully.")

        print("Test Case 19: View Brand Products - Passed!")

