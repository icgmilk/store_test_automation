from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.page_base import ActionUtils

class HomePage(ActionUtils):

    def __init__(self, driver):
        """ Constructor of the HomePage class 
        Args:
            driver (WebDriver): The instance of the WebDriver
        """
        super().__init__(driver)
        self.search_text_field_locator = (By.ID, "ns-search-input")
        self.search_button_locator = (By.XPATH, '//i[@class="ico ico-search"]')

    def input_search_text(self, text):
        """ Input the search text
        Args:
            text (str): The search text
        """
        wait = WebDriverWait(self.driver, 10)
        text_element = wait.until(EC.presence_of_element_located(self.search_text_field_locator))
        text_element.send_keys(text)

    def click_search_button(self):
        """ Click the search button """
        button_element = self.find_clickable_element(self.search_button_locator)
        button_element.click()


        