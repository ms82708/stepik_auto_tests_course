import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math

with webdriver.Chrome() as driver:

    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    waiter = WebDriverWait(driver, 30)

    # Ожидать пока не появится текст "$100"
    waiter.until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    x = driver.find_element(By.ID, 'input_value').text
    y = math.log(abs(12 * math.sin(int(x))))
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.ID, 'solve').click()
    time.sleep(3)
