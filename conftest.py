import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
    parser.addoption('--headless', action='store_true', help="Run browser in headless mode")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options)
    elif browser_name == "firefox":
        options_firefox = OptionsFirefox()
        if headless:
            options_firefox.add_argument("--headless")
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def user_language(request):
    return request.config.getoption("language")
