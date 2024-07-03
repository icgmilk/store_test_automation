import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_result_page import SearchResultPage
from pages.first_goods_page import FirstGoodsPage
from pages.cart_page import CartPage
from dotenv import load_dotenv

load_dotenv()
login_phone = os.getenv('PYTEST_LOGIN_PHONE')
login_password = os.getenv('PYTEST_LOGIN_PASSWORD')
login_url = 'https://www.tvgame.com.tw/V2/Login/Index/'

def driver_setup():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    return driver

def test_login_then_add_product_to_cart():
    """ 測試登入後搜尋商品後加入到購物車 
    1. 進入登入頁面
    2. 輸入手機號碼
    3. 輸入密碼
    4. 搜尋商品
    5. 點擊第一個商品
    6. 進到商品頁面點擊加入購物車

    """
    driver = driver_setup()
    loginpage = LoginPage(driver)
    homepage = HomePage(driver)
    search_result_page = SearchResultPage(driver)
    first_goods_page = FirstGoodsPage(driver)
    cart_page = CartPage(driver)
    
    #進入登入頁面
    driver.get(login_url)

    #輸入手機號碼
    loginpage.input_cell_phone(login_phone)
    loginpage.click_login_register_button()

    #輸入密碼
    loginpage.input_password(login_password)
    
    #避免reCAPTCHA
    time.sleep(3)
    loginpage.click_login_button()
    loginpage.wait_login()

    #搜尋商品
    homepage.input_search_text('瑪利歐賽車8 豪華版')
    homepage.click_search_button()

    #點擊第一個商品
    search_result_page.click_first_goods()

    #進到商品頁面點擊加入購物車
    goods_title = first_goods_page.get_goods_title()
    first_goods_page.click_add_to_cart_button()
    first_goods_page.click_cart_button()

    #確認商品是否成功加入購物車
    assert cart_page.check_goods_title(goods_title)
