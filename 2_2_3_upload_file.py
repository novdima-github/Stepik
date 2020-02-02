from selenium import webdriver
import time

try:
    browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    f_name = browser.find_element_by_css_selector("["
                                                  "name=firstname]").send_keys("Name")
    l_name = browser.find_element_by_css_selector("["
                                                  "name=lastname]").send_keys(
        "Last Name")
    email = browser.find_element_by_css_selector("["
                                                  "name=email]").send_keys(
        "email@dot.com")


    import os
    current_dir = os.path.abspath(os.path.dirname(
        __file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir,
                             'file.txt')  # добавляем к этому пути имя файла

    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

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
