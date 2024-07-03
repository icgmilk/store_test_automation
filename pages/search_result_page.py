from selenium.webdriver.common.by import By
from pages.page_base import ActionUtils


class SearchResultPage(ActionUtils):
    def __init__(self, driver):
        """ Constructor of the SearchResultPage class
        Args:
            driver (WebDriver): The instance of the WebDriver
        """
        super().__init__(driver)
        self.driver = driver
        self.commodity_locator = (By.XPATH, '(//img[@class = "product-card__vertical__media product-card__vertical__media-tall"])[1]')

    def click_first_goods(self):
        """ Click the first goods """
        goods_element = self.find_clickable_element(self.commodity_locator)
        goods_element.click()

