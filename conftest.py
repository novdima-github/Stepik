# browser = webdriver.Firefox(executable_path="d:\\Soft\\geckodriver.exe")

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
browser = webdriver.Chrome(options=options)

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", 'ru')
browser = webdriver.Firefox(firefox_profile=fp)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(executable_path="d:\\Soft\\chromedriver.exe")
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path="d:\\Soft\\geckodriver.exe")
    else:
        raise pytest.UsageError("--browser_name option should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()