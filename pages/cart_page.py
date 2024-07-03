from selenium.webdriver.common.by import By
from pages.page_base import ActionUtils

class CartPage(ActionUtils):
    def __init__(self, driver):
        """ Constructor of the CartPage class
        Args:
            driver (WebDriver): The instance of the WebDriver
        """
        super().__init__(driver)
        self.driver = driver
    
    def check_goods_title(self, goods_title):
        """ Check the goods title
        Args:
            goods_title (str): The goods title
        Returns:
            bool: The result
        """
        try:
            #檢查title是否存在購物車內
            goods_title_element = self.find_visible_element((By.XPATH, f'''//a[text()="{goods_title}"] '''))
            return True 
        except:
            return False

    
        

    