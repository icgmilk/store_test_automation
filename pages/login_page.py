from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.page_base import ActionUtils

class LoginPage(ActionUtils):
    def __init__(self, driver):
        """ Constructor of the LoginPage class
        Args:
            driver (WebDriver): The instance of the WebDriver
        """
        super().__init__(driver)
        self.cell_phone_locator = (By.NAME, 'cellPhone')
        self.password_locator = (By.NAME, 'password')
        self.login_register_button_locator = (By.XPATH, '//button[text()="登入/註冊"]')
        self.login_button_locator = (By.XPATH, '//button[text()="登入"]')


    def input_cell_phone(self, cell_phone):
        """ Input the cell phone number
        Args:
            cell_phone (str): The cell phone number
        """
        cell_phone_element = self.find_visible_element(self.cell_phone_locator)
        cell_phone_element.send_keys(cell_phone)

    def input_password(self, password):
        """ Input the password
        Args:
            password (str): The password
        """
        password_element = self.find_visible_element(self.password_locator)
        password_element.send_keys(password)

    def click_login_register_button(self):
        """ Click the login/register button """
        login_register_button_element = self.find_clickable_element(self.login_register_button_locator)
        login_register_button_element.click()

    def click_login_button(self):
        """ Click the login button """
        login_button_element = self.find_clickable_element(self.login_button_locator)
        login_button_element.click()