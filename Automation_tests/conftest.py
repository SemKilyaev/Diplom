import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose driver: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("browser")
    if browser == "firefox":
        print("\nstart firefox driver for test..")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        yield
        driver.delete_all_cookies()
        driver.quit()

    elif browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.delete_all_cookies()
        request.cls.driver = driver 
        print("Current session is {}".format(driver.session_id))
        yield
        driver.delete_all_cookies()
        driver.quit()
