from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.page_base import ActionUtils

class CartPage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.goods_title_locator = (By.XPATH, '//a[contains (@class, "TitleLink")]')
        self.goods_price_locator = (By.XPATH, '(//div[contains (@class, "currency__Wrapper")])[1]')
        self.goods_count_locator = (By.XPATH, '//input[contains (@class, "Input")]')

    def get_goods_title(self):
        goods_title_element = self.find_visible_element(self.goods_title_locator)
        return goods_title_element.text
    
    def get_goods_price(self):
        goods_price_element = self.find_visible_element(self.goods_price_locator)
        return goods_price_element.text

    def get_goods_count(self):
        goods_count_element = self.find_visible_element(self.goods_count_locator)
        return goods_count_element.get_attribute('value')
        

    