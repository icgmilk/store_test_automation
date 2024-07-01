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
from pages.cart_page import CartPage
from dotenv import load_dotenv
import os

load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()  

login_phone = os.getenv('PYTEST_LOGIN_PHONE')
login_password = os.getenv('PYTEST_LOGIN_PASSWORD')

def find_element(by, value):
    return (by, value)
def test_login_then_add_product_to_cart():
    #進入登入頁面
    url_login = 'https://www.tvgame.com.tw/V2/Login/Index/'
    driver.get(url_login)

    #輸入手機號碼
    loginpage = LoginPage(driver)
    loginpage.input_cell_phone(login_phone)
    loginpage.click_login_register_button()

    #輸入密碼
    loginpage.input_password(login_password)
    time.sleep(3)
    loginpage.click_login_button()

    #搜尋商品

    homepage = HomePage(driver)
    homepage.wait_login()
    homepage.input_search_text('瑪利歐賽車8 豪華版')
    homepage.click_search_button()

    #點擊第一個商品
    search_result_page = SearchResultPage(driver)
    search_result_page.click_first_goods()

    #進到商品頁面點擊加入購物車
    first_goods_page = FirstGoodsPage(driver)

    good_title = first_goods_page.get_goods_title()


    first_goods_page.click_add_to_cart_button()
    first_goods_page.click_cart_button()

    cart_page = CartPage(driver)

    assert good_title == cart_page.get_goods_title()
