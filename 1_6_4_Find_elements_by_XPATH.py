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
try:
    browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    # button = browser.find_element_by_css_selector("div:nth-child(6) button:nth-child(3)")
    button = browser.find_element_by_xpath("//*[text()='Submit']")
    button.click()
    alert = browser.switch_to.alert
    text = alert.text
    help(text)
    print(text[-19:])
    alert.accept()
    print("Success!")

finally:
    time.sleep(5)
    browser.quit()
