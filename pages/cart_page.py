from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.page_base import ActionUtils

class CartPage(ActionUtils):
    def __init__(self, driver):
        """ Constructor of the CartPage class
        Args:
            driver (WebDriver): The instance of the WebDriver
        """
        super().__init__(driver)
        self.driver = driver
        self.goods_title_locator = (By.XPATH, '//a[contains (@class, "TitleLink")]')
        self.goods_price_locator = (By.XPATH, '(//div[contains (@class, "currency__Wrapper")])[1]')
        self.goods_count_locator = (By.XPATH, '//input[contains (@class, "Input")]')

    def get_goods_title(self):
        """ Get the goods title
        Returns:
            str: The goods title
        """
        goods_title_element = self.find_visible_element(self.goods_title_locator)
        return goods_title_element.text
    
    def get_goods_price(self):
        """ Get the goods price
        Returns:
            str: The goods price
        """
        goods_price_element = self.find_visible_element(self.goods_price_locator)
        return goods_price_element.text

    def get_goods_count(self):
        """ Get the goods count
        Returns:
            str: The goods count
        """
        goods_count_element = self.find_visible_element(self.goods_count_locator)
        return goods_count_element.get_attribute('value')
        

    