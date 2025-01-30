import pytest
from config.config import Config
from pages.view_category_products_page import CategoryPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestCategoryProducts:
    def test_view_category_products(self):
        category_page = CategoryPage(self.driver)

        self.driver.get(Config.BASE_URL)

        self.driver.execute_script("window.scrollBy(0, 300)")
        
        assert category_page.verify_categories_visible(), "Categories are not visible in the left sidebar."

        category_page.click_women_category()
        category_page.click_dress_category()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(category_page.CATEGORY_PAGE_HEADER_WOMEN)
        )
        assert category_page.verify_category_page_displayed(), "Category page for 'Women - Dress Products' is not displayed."

        screenshot_path = take_screenshot(self.driver, "screenshots", "WomenDressCategoryPage")
        print(f"Screenshot saved at: {screenshot_path}")

        print("Attempting to click on 'Men' category...")

        category_page.click_men_category()

        category_page.click_men_sub_category()

        print("Verifying 'Men' sub-category page is displayed...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(category_page.CATEGORY_PAGE_HEADER_MEN)
        )
        assert category_page.check_category_page_displayed(), "Category page for 'Men' sub-category is not displayed."

        screenshot_path = take_screenshot(self.driver, "screenshots", "MenSubCategoryPage")
        print(f"Screenshot saved at: {screenshot_path}")

        print("Test Case 18: View Category Products - Passed!")
