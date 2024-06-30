import pytest
import time
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
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_result_page import SearchResultPage
from pages.first_goods_page import FirstGoodsPage



options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



def find_element(by, value):
    return (by, value)



#進入登入頁面
url = 'https://www.tvgame.com.tw/V2/Login/Index/'
driver.get(url)
time.sleep(2)

#輸入手機號碼
loginpage = LoginPage(driver)
loginpage.input_cell_phone('cellphone')
loginpage.click_login_register_button()
time.sleep(3)

#輸入密碼
loginpage.input_password('password')
loginpage.click_login_button()
time.sleep(15)

#搜尋商品
homepage = HomePage(driver)
homepage.input_search_text('瑪利歐賽車8 豪華版')
homepage.click_search_button()
time.sleep(4)

#點擊第一個商品
search_result_page = SearchResultPage(driver)
search_result_page.click_first_goods()
time.sleep(3)

#進到商品頁面點擊加入購物車
first_goods_page = FirstGoodsPage(driver)
first_goods_page.click_add_to_cart_button()
time.sleep(3)