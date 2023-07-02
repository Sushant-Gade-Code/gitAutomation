import pytest

from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
        print("Headless Mode")
        opt=webdriver.ChromeOptions()
        opt.add_argument("headless")
        driver=webdriver.Chrome(options=opt)
    driver.minimize_window()
    return driver
