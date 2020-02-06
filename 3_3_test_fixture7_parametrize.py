import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("d:\Soft\chromedriver.exe")
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]) #
def test_correct_feedback(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    print(answer)

    time.sleep(1)
    browser.find_element_by_css_selector(".textarea").send_keys(answer)
    time.sleep(1)
    browser.find_element_by_css_selector(".submit-submission").click()
    time.sleep(1)
    price = WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'smart-hints__hint'), 'Correct!')
    )
    correct = browser.find_element_by_class_name('smart-hints__hint').text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Correct!" == correct
    print("Success!")