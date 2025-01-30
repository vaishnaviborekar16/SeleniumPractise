from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class ProductsReviewPage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    ALL_PRODUCTS_HEADER = (By.XPATH, "//h2[contains(text(), 'All Products')]")
    PRODUCT_LIST = (By.XPATH, "//div[@class='features_items']//div[@class='product-image-wrapper']")
    FIRST_PRODUCT_VIEW_BUTTON = (By.XPATH, "(//a[contains(text(), 'View Product')])[1]")
    REVIEW_HEADER = (By.XPATH, "/html/body/section/div/div/div[2]/div[3]/div[1]/ul/li/a")
    ENTER_NAME = (By.XPATH, "//*[@id='name']")
    ENTER_EMAIL = (By.XPATH, "//*[@id='email']")
    ENTER_REVIEW = (By.XPATH, "//*[@id='review']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='button-review']")
    SUCCESS_MESSAGE = (By.XPATH, "//span[text()='Thank you for your review.']")
    
    def navigate_to_products_page(self):
        self.driver.find_element(*self.PRODUCTS_BUTTON).click()

    def verify_all_products_header(self):
        header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ALL_PRODUCTS_HEADER)
        )
        return header.is_displayed()

    def click_first_product_view_button(self):
        self.driver.find_element(*self.FIRST_PRODUCT_VIEW_BUTTON).click()

    def verify_review_section_visible(self):
        review_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.REVIEW_HEADER)
        )
        return review_header.is_displayed()

    def submit_review(self, name, email, review):
        self.driver.find_element(*self.ENTER_NAME).send_keys(name)
        self.driver.find_element(*self.ENTER_EMAIL).send_keys(email)
        self.driver.find_element(*self.ENTER_REVIEW).send_keys(review)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def verify_success_message(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
        return success_message.is_displayed()
