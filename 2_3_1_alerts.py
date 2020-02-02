"""
alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()

confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    submit = browser.find_element_by_css_selector("[type=submit]").click()
    confirm = browser.switch_to.alert
    confirm.accept()

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
