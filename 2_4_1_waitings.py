"""
browser.switch_to.window(window_name)
first_window = browser.window_handles[0]
new_window = browser.window_handles[1]
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    button = browser.find_element_by_id('book').click()

    price = browser.find_element_by_id('input_value').text
    res = calc(price)
    field = browser.find_element_by_id("answer").send_keys(res)
    submit = browser.find_element_by_css_selector("[type=submit]").click()

    alert = browser.switch_to.alert
    text = alert.text
    help(text)
    print(text[-18:])
    alert.accept()
    print("success!")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
