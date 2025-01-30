import pytest
from config.config import Config
from pages.subscription_in_cart_page import HomePage
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestSubscription:
    @pytest.mark.parametrize(
        "url", [Config.BASE_URL]
    )
    def test_verify_subscription_in_cart(self, url):
        home_page = HomePage(self.driver)
        home_page.visit(url)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page is successfully loaded.")
        home_page.click_cart_button()
        print("Clicked on Cart button.")
        assert home_page.is_element_visible(home_page.SUBSCRIPTION_TEXT), "'SUBSCRIPTION' text is not visible."
        print("Subscription section is visible.")
        email = "alexpeter234@gmail.com"
        home_page.enter_subscription_email(email)
        home_page.click_subscribe()
        print("Email entered and Subscribe button clicked.")
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="subscription_success_in_cart"
        )
        print(f"Screenshot taken: {screenshot_path}")

        print("Test for subscription functionality passed.")

       
       
