"""
find_element_by_id
find_element_by_id
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
_________________________
from selenium.webdriver.common.by import By

example: button = browser.find_element(By.ID, "submit_button")

By.ID – поиск по уникальному атрибуту id элемента;
By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
By.XPATH – поиск элементов с помощью языка запросов XPath;
By.NAME – поиск по атрибуту name элемента;
By.TAG_NAME – поиск по названию тега;
By.CLASS_NAME – поиск по атрибуту class элемента;
By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    x_element = browser.find_element_by_id("treasure")
    atribute = x_element.get_attribute("valuex")

    y = calc(atribute)
    print(y)
    text_field = browser.find_element_by_css_selector("#answer")
    text_field.send_keys(y)
    chbox = browser.find_element_by_css_selector("#robotCheckbox").click()
    rb = browser.find_element_by_css_selector("#robotsRule").click()
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

