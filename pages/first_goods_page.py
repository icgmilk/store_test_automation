from selenium.webdriver.common.by import By
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
        self.goods_title_locator = (By.XPATH, '//h1[@class = "salepage-title"]')
        self.goods_price_locator = (By.XPATH, '//meta[@itemprop = "price"]')
        self.goods_count_locator = (By.XPATH, '//input[@class = "qty-number-input ng-pristine ng-valid ng-not-empty ng-valid-min ng-valid-max ng-touched"]"]')
        self.cart_button_locator = (By.XPATH, '//i[@class = "ico ico-shopping user-interaction-icon"]')

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

    def click_add_to_cart_button(self):
        """ Click the add to cart button """
        add_to_cart_button_element = self.find_clickable_element(self.add_to_cart_button_locator)
        add_to_cart_button_element.click()

    def click_cart_button(self):
        """ Click the cart button """
        cart_button_element = self.find_clickable_element(self.cart_button_locator)
        cart_button_element.click()