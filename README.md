# store_test_automation

## 實作基本購物流程的自動化測試

選擇網站: [普雷伊電視遊樂器專賣店](https://www.tvgame.com.tw/?lang=zh-TW)
使用[Python](https://www.python.org/),[Pytest](https://docs.pytest.org/en/8.2.x/),[Selenium](https://www.selenium.dev/)
## 安裝說明

    $ pip install -r requirements.txt

## 執行說明
將專案clone下來後在test.py目錄下開啟終端

輸入
```
pytest test.py
```
## 專案結構說明

```
└──Store_Test_Automation
│    │
│    ├── pages
│    │   └── cart_page.py
│    │   └── first_goods_page.py
│    │   └── home_page.py
│    │   └── login_page.py
│    │   └── page_base.py
│    │   └── search_result_page.py
│    │ 
│    ├── tests 
│    │  └── __init__.py
│    │  └── test.py
│    │ 
│    ├── pytest.ini│ 
│    │ 
│    ├── README.md
│    │ 
└──  └── requirements.txt
```
## 驗證項目
    驗證購物網站的流程
    * 登入
    * 搜尋商品
    * 點擊第一個商品
    * 加入購物車

