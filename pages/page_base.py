from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionUtils():
    def __init__(self, driver):
        """ Constructor of the ActionUtils class
        Args:
            driver (WebDriver): The instance of the WebDriver
        """
        self.driver = driver

    def find_visible_element(self, locator, timeout=10):
        """ Find the visible element
        Args:
            locator (tuple): The locator of the element
            timeout (int): The time to wait for the element
        Returns:
            WebElement: The element
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator, timeout=10):
        """ Find the clickable element
        Args:
            locator (tuple): The locator of the element
            timeout (int): The time to wait for the element
        Returns:
            WebElement: The element
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )