import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_test1(self):
        try:
            browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(
                "input[placeholder='Input your first name']")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(
                "input[placeholder='Input your last name']")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(
                "input[placeholder='Input your email']")
            input3.send_keys("Smolensk@tut.by")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text
            print("Success!")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_test2(self):

        browser = webdriver.Chrome("f:\Дима\chromedriver.exe")
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(
            "input[placeholder='Input your name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            "input[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(
            "input[placeholder='Input your email']")
        input3.send_keys("Smolensk@tut.by")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        print("Success!")


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()