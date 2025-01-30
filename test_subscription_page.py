import pytest
from config.config import Config
from pages.subscription_page import HomePage
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestSubscription:
    @pytest.mark.parametrize(
        "url", [Config.BASE_URL]
    )
    def test_verify_subscription(self, url):
        home_page = HomePage(self.driver)
        home_page.visit(url)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page is successfully loaded.")

        home_page.scroll_to_footer()
        print("Scrolled to footer.")

        assert home_page.is_element_visible(home_page.SUBSCRIPTION_TEXT), "'SUBSCRIPTION' text is not visible."
        print("Subscription section is visible.")
        email = "alex12547@gmail.com"
        home_page.enter_subscription_email(email)
        home_page.click_subscribe()
        print("Email entered and Subscribe button clicked.")
        screenshot_path_before = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="subscription_done"
        )
        print(f"Screenshot taken after checking success message: {screenshot_path_before}")
