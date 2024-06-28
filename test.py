import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
import time
driver = webdriver.Chrome('driver/chromedriver.exe')

#進入登入頁面
url = 'https://www.tvgame.com.tw/V2/Login/Index/'
driver.get(url)
time.sleep(2)

#輸入手機號碼
phone = driver.find_element(By.NAME, 'cellPhone')
phone.send_keys('0937058761')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/button').click()
time.sleep(3)

#輸入密碼
password = driver.find_element(By.NAME, 'password')
password.send_keys('test1101')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/form/button').click()
time.sleep(8)

#搜尋商品
goods_name = driver.find_element(By.NAME, 'q')
goods_name.send_keys('瑪利歐賽車8 豪華版')
time.sleep(1)
goods_name.send_keys(Keys.ENTER)
time.sleep(4)

#點擊第一個商品
first_goods = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/ul/li[1]/div/a/div/div[1]/div/figure/img')
first_goods.click()
time.sleep(3)

#進到商品頁面點擊加入購物車
shopping_cart = driver.find_element(By.XPATH, '//*[@id="ns-add-to-cart"]/div/div[2]/div[2]/button[1]')
shopping_cart.click()
time.sleep(3)