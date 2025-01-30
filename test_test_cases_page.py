import pytest
from config.config import Config
from pages.test_case_page import CasesPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.take_screenshot import take_screenshot


@pytest.mark.usefixtures("init_driver")
class TestTestCasesPage:
    @pytest.mark.parametrize(
        "url", [Config.BASE_URL]
    )
    def test_verify_test_cases_page(self, url):
        cases_page = CasesPage(self.driver)

        # Navigate to the base URL
        cases_page.visit(url)
        assert "Automation Exercise" in self.driver.title, "Home page title does not match."
        print("Home page is successfully loaded.")

        cases_page.click_test_cases_button()
        
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CasesPage.PAGE_HEADER)
        )

        assert cases_page.verify_test_cases_page_visible(), "Test Cases page is not visible."
        screenshot_path = take_screenshot(
            self.driver, save_path="screenshots", filename_prefix="test_cases_page"
        )
        print(f"Screenshot taken: {screenshot_path}")
        print("Test for Test Cases page passed.")
