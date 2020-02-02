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
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
    browser.get("http://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.CSS_SELECTOR, "input[type=text]")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

    alert = browser.switch_to.alert
    text = alert.text
    help(text)
    print(text[-17:])
    alert.accept()
    print("success!")

finally:
    time.sleep(5)
    browser.quit()
