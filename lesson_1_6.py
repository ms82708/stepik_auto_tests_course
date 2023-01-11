import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/registration2.html')
    driver.maximize_window()
    time.sleep(1)

    input1 = driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CSS_SELECTOR, '.form-control.third')
    input3.send_keys("15@Smolensk")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    time.sleep(2)
    result = driver.find_element(By.TAG_NAME, 'h1').text
    assert result == 'Congratulations! You have successfully registered!'
    print("Test Ok")
    time.sleep(2)
