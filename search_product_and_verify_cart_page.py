from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SearchCartPage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_HEADER = (By.XPATH, "//h2[contains(text(), 'Searched Products')]")
    PRODUCT_LIST = (By.XPATH, "//div[@class='product-overlay']")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//a[contains(text(), 'Add to cart')]")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='cartModal']/div/div/div[3]/button")
    LOGIN_BUTTON = (By.LINK_TEXT, "Signup / Login")
    LOGIN_EMAIL = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]")
    LOGIN_PASSWORD = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
    LOGGED_IN_AS_TEXT = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
    CART_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a")
    REMOVE_BUTTONS = (By.XPATH, "//a[@class='cart_quantity_delete']")
    CART_EMPTY_MESSAGE = (By.XPATH, "//*[@id='empty_cart']/p")
    CART_ROWS = (By.XPATH, "//*[@id='cart_items']/tbody/tr")

    # Actions
    def navigate_to_products_page(self):
        self.click(self.PRODUCTS_BUTTON)

    def search_for_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def verify_search_results_visible(self):
        return self.is_element_visible(self.SEARCHED_PRODUCTS_HEADER)

 
    def add_all_products_to_cart(self):
        """Adds all products displayed in the search results to the cart."""
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)

        for button in add_to_cart_buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((button)))
    
                ActionChains(self.driver).move_to_element(button).perform()

                button.click()
                print("Added a product to the cart.")

                WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CONTINUE_BUTTON)
                ).click()
            except Exception as e:
                print(f"Error adding product to cart: {e}")       
  
      
        
    def login(self,email,password):
        self.click(self.LOGIN_BUTTON)
        self.enter_text(self.LOGIN_EMAIL, email)
        self.enter_text(self.LOGIN_PASSWORD,password)
        self.click(self.LOGIN_SUBMIT_BUTTON)
        
    
    def verify_logged_in(self):
        try:
            element=self.find_web_element(self.LOGGED_IN_AS_TEXT)
            return element.is_displayed()
        except:
            return False    
        
              
    def navigate_to_cart_page(self):
        self.click(self.CART_BUTTON)
        
    def remove_all_products_from_cart(self):
        try:
            remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
            if remove_buttons:
                for button in remove_buttons:
                    button.click() 
                    print("Removed a product from the cart.")
                else:
                    print("No products found in the cart to remove.")
        except Exception as e:
            print(f"Error while removing products: {e}")

  
            
    def is_cart_empty(self):
        try:
            empty_cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_EMPTY_MESSAGE)
            )
            return empty_cart.is_displayed()
        except:
            product_rows = self.driver.find_elements(*self.CART_ROWS)
            return len(product_rows) == 0