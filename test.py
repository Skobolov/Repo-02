import allure
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
    @allure.feature("Open pages")
    @allure.story("Open pages Google.com")
    @allure.severity("blocker")
    def test_google_search(self):
        self.driver.get("https://google.com")
#        with allure.step("Делаем скриншот"):s
#            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Google"

    time.sleep(5)
    driver.quit()

