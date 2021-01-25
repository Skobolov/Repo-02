
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
        
capabilities = {
    "browserName": "chrome",
    "browserVersion": "85.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}


class TestPageSearch:
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)

    def test_google_search(self):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"

    time.sleep(5)
    driver.quit()

