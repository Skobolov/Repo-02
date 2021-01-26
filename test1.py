import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = {
    "browserName": "chrome",
    "browserVersion": "85.0",
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

def test_title():
    driver.get('https://www.google.com/')
    assert "Google" in driver.title

time.sleep(10)
driver.quit()