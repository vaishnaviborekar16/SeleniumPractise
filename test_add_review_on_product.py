import pytest
from config.config import Config
from pages.add_review_on_product_page import ProductsReviewPage
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestProductsReview:
    @pytest.mark.parametrize("url", [Config.BASE_URL])
    def test_verify_review_functionality(self, url):
        """Test to verify the review functionality on the Products page."""
        review_page = ProductsReviewPage(self.driver)
        review_page.visit(url)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page successfully loaded.")

        review_page.navigate_to_products_page()

        review_page.driver.execute_script("window.scrollBy(0, 400)")

        assert review_page.verify_all_products_header(), "All Products header is not visible."
        print("Navigated to All Products page.")

        review_page.click_first_product_view_button()
        print("Navigated to the first product's details page.")

        assert review_page.verify_review_section_visible(), "'Write Your Review' section is not visible."
        print("'Write Your Review' section is visible.")

        name = "John Doe"
        email = "johndoe@example.com"
        review_text = "This is a fantastic product. Highly recommended!"
        review_page.submit_review(name, email, review_text)
        print("Review form submitted.")

        assert review_page.verify_success_message(), "Success message 'Thank you for your review.' is not visible."
        print("Success message verified.")

        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="review_success"
        )
        print(f"Screenshot taken: {screenshot_path}")

        print("Test Case 21: Test for review functionality passed.")
