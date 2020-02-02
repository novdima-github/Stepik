"""
browser.switch_to.window(window_name)
first_window = browser.window_handles[0]
new_window = browser.window_handles[1]
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element_by_class_name("trollface").click()
    browser.switch_to.window(browser.window_handles[1])
    number = browser.find_element_by_id("input_value").text
    res = calc(number)
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
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
