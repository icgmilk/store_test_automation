import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome('driver/chromedriver')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_enter(driver):
    driver.get("https://www.tvgame.com.tw/")
    assert driver.title == "普雷伊電視遊樂器專賣店"

def test_search(driver):
    driver.get("https://www.tvgame.com.tw/")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("switch")
    search.send_keys(Keys.RETURN)
    time.sleep(3)
    assert "switch" in driver.title

def test_click_commodity(driver):
    driver.get("https://www.tvgame.com.tw/v2/Search?q=switch&shopId=2315")
    click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/ul/li[1]/div/a/div/div[1]/div/figure/img')
    click.click()
    time.sleep(3)
    assert "【NS】" in driver.title

def test_add_to_cart(driver):
    driver.get("https://www.tvgame.com.tw/SalePage/index/8912697")
    add = driver.find_element(By.XPATH, '//*[@id="ns-add-to-cart"]/div/div[2]/div[2]/button[1]')
    add.click()
    time.sleep(3)

    cart = driver.find_element(By.XPATH, '//*[@id="layout-header-fix"]/div/nav/ul/li[3]/a/span')
    assert int(cart) == 1

def test_login(driver):
    # 進入登入頁面
    url = 'https://www.tvgame.com.tw/V2/Login/Index/'
    driver.get(url)
    time.sleep(2)

    # 輸入手機號碼
    phone = driver.find_element(By.NAME, 'cellPhone')
    phone.send_keys('0937xxxxxxxx')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/button').click()
    time.sleep(3)

    # 輸入密碼
    password = driver.find_element(By.NAME, 'password')
    password.send_keys('testxxxxxxxxx')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/form/button').click()
    time.sleep(8)

    login_text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/header/div[1]/div/div/nav/ul/li[2]/div/ul/li[5]/a').text
    assert login_text == "會員登出", f"登出連結的文本應為 '會員登出'，但實際為 '{login_text}'"
