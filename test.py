import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.tvgame.com.tw/V2/Login/Index/'
web_driver_wait = WebDriverWait(driver, 1)
driver.get(url)

locator = (By.NAME, 'cellPhone')
def find_element(locator]):
    web_driver_wait.until(method=EC.element_to_be_clickable((by, value))


web_driver_wait.until(method=EC.element_to_be_clickable((By.NAME, 'ce')),
message= "錯誤"
).send_keys('0937058761')
