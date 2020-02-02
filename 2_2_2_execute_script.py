import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    input_value = browser.find_element_by_id("input_value").text
    res = calc(input_value)
    field = browser.find_element_by_id("answer").send_keys(res)

    submit = browser.find_element_by_css_selector("[type=submit]")
    browser.execute_script("window.scrollBy(0, 100);")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    time.sleep(5)
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radio_button = browser.find_element_by_css_selector("[for=robotsRule]").click()
    submit.click()

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
