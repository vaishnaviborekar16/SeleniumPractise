import pytest
from config.config import Config
from pages.scroll_up_down_without_arrow_page import ScrollWithoutArrowPage
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestScrollWithoutArrow:

    def test_scroll_up_without_arrow_and_down(self):
        page = ScrollWithoutArrowPage(self.driver)
        page.visit(Config.BASE_URL)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page successfully loaded.")
        
        page.scroll_to_bottom()
        print("Scrolled to the bottom of the page.")

        page.verify_subscription_visible()
        print("'SUBSCRIPTION' section is visible.")
        
        page.scroll_to_top()
        print("Scrolled up to the top of the page.")

        page.verify_practice_website_visible()
        print("'Full-Fledged practice website for Automation Engineers' text is visible.")

        screenshot_path = take_screenshot(self.driver, "screenshots", "ScrollWithoutArrowFunctionality")
        print(f"Screenshot saved at: {screenshot_path}")

        print("Test passed 26 : Page scrolled down and up successfully without using the arrow button.")
