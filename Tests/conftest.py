import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=chrome,
                     help="Choose browser: chrome or firefox")

@pytest.fixture()
def driver():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
        )
    yield driver
    driver.quit()


