from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.page_base import ActionUtils

class FirstGoodsPage(ActionUtils):
    def __init__(self, driver):
        """ Constructor of the FirstGoodsPage class
        Args:
            driver (WebDriver): The instance of the WebDriver
        """
        super().__init__(driver)
        self.driver = driver
        self.add_to_cart_button_locator = (By.XPATH, '//span[text()="加入購物車"]')
    
    def click_add_to_cart_button(self):
        """ Click the add to cart button """
        add_to_cart_button_element = self.find_clickable_element(self.add_to_cart_button_locator)
        add_to_cart_button_element.click()
