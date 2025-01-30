from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BrandPage(BasePage):
    BRANDS_SECTION = (By.XPATH, "//div[@class='brands-name']")
    BRAND_1_LINK = (By.XPATH, "//div[@class='brands-name']//ul/li[1]/a")
    BRAND_2_LINK = (By.XPATH, "//div[@class='brands-name']//ul/li[2]/a")
    BRAND_PAGE_HEADER = (By.XPATH, "//h2[@class='title text-center']")

    def verify_brands_visible(self):
        return self.is_element_visible(self.BRANDS_SECTION)

    def click_brand_1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BRAND_1_LINK))
        self.driver.execute_script("window.scrollBy(0, 300)")
        self.click(self.BRAND_1_LINK)

    def click_brand_2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BRAND_2_LINK))
        self.driver.execute_script("window.scrollBy(0, 300)")
        self.click(self.BRAND_2_LINK)

    def verify_brand_page_header(self):
        return self.is_element_visible(self.BRAND_PAGE_HEADER)
       
