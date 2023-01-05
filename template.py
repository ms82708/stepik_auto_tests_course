import select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pprint import pprint
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import sys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime as dt
from calendar import monthrange
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import os

# pprint()
start = time.time()

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')  # Переключение в фоновый режим
with webdriver.Chrome() as driver:
    # with webdriver.Chrome(options=options_chrome) as driver: # без отрисовки браузера
    driver.get('https://parsinger.ru/expectations/3/index.html')
    #driver.maximize_window()
    waiter = WebDriverWait(driver, 30)  # ожидание до 30 сек

    # button_cl = waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="btn"]'))).click()
    # element = waiter.until(EC.title_is('345FDG3245SFD'))
    # code = driver.find_element(By.CSS_SELECTOR, '[id="result"]').text
    # print(code)
    time.sleep(3)