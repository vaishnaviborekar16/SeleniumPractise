import pytest
from config.config import Config
from pages.scroll_up_down_using_arrow_page import HomePage
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestHomePage:

    def test_scroll_and_verify(self):
        home_page = HomePage(self.driver)

        home_page.visit(Config.BASE_URL)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page successfully loaded.")

        home_page.scroll_to_bottom()
        print("Scrolled to the bottom of the page.")

        home_page.verify_subscription_visible()
        print("'SUBSCRIPTION' section is visible.")

        home_page.click_scroll_up_arrow()
        print("Clicked on the scroll-up arrow.")
        
        screenshot_path = take_screenshot(self.driver, "screenshots", "ScrollUpDownUsingArrow")
        print(f"Screenshot saved at: {screenshot_path}")
        
        home_page.verify_practice_website_visible()
        print("'Full-Fledged practice website for Automation Engineers' is visible.")

        print("Test passed 25: Page scrolled and elements verified successfully.")
