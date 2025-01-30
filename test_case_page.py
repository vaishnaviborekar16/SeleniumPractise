from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CasesPage(BasePage):
    TEST_CASES_BUTTON = (By.LINK_TEXT, "Test Cases")
    PAGE_HEADER = (By.XPATH, "//*[@id='form']/div/div[1]/div/h2/b")  
    def click_test_cases_button(self):
        self.click(self.TEST_CASES_BUTTON)
        print("Clicked on 'Test Cases' button.")

    def verify_test_cases_page_visible(self):
        header = self.find_web_element(self.PAGE_HEADER)
        if header:
            print(f"Header Text: {header.text}")
        else:
            print("Header not found.")
        return header is not None
