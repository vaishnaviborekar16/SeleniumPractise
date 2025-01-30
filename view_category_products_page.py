from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CategoryPage(BasePage):
    CATEGORIES_SECTION = (By.XPATH, "//div[@class='left-sidebar']")
    WOMEN_CATEGORY = (By.XPATH, "//*[@id='accordian']/div[1]/div[1]/h4/a")
    WOMEN_DRESS_LINK = (By.XPATH, "//*[@id='Women']/div/ul/li[1]/a")
    CATEGORY_PAGE_HEADER_WOMEN = (By.XPATH, "/html/body/section/div/div[2]/div[2]/div/h2")
    MEN_CATEGORY = (By.XPATH, "//*[@id='accordian']/div[2]/div[1]/h4/a")
    SUB_CATEGORY_MEN_LINK = (By.XPATH, "//*[@id='Men']/div/ul/li[1]/a")
    CATEGORY_PAGE_HEADER_MEN = (By.XPATH, "/html/body/section/div/div[2]/div[2]/div/h2")

    def verify_categories_visible(self):
        return self.is_element_visible(self.CATEGORIES_SECTION)

    def click_women_category(self):
        self.click(self.WOMEN_CATEGORY)

    def click_dress_category(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.WOMEN_DRESS_LINK))
        self.click(self.WOMEN_DRESS_LINK)

    def verify_category_page_displayed(self):
        return self.is_element_visible(self.CATEGORY_PAGE_HEADER_WOMEN)

    def click_men_category(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.MEN_CATEGORY))
        self.click(self.MEN_CATEGORY)

    def click_men_sub_category(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUB_CATEGORY_MEN_LINK))
        self.click(self.SUB_CATEGORY_MEN_LINK)

    def check_category_page_displayed(self):
        return self.is_element_visible(self.CATEGORY_PAGE_HEADER_MEN)
