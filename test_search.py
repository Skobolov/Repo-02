import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver

exec_path="drivers/chromedriver.exe"

class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)

    def teardown(self):
        self.driver.quit()

    @allure.feature("Open pages")
    @allure.story("Open pages Google.com")
    @allure.severity("blocker")
    def test_google_search(self):
        self.driver.get("https://google.com")
        with allure.step("Делаем скриншот"):
            allure.attach(self.driver.get_screenshot_as_png(), name = "Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Google"

    @allure.feature("Open pages")
    @allure.story("Open pages Yandex.ru")
    @allure.severity("critical")
    def test_yandex_search(self):
        self.driver.get("https://yandex.ru")
        with allure.step("Делаем скриншот"):
            allure.attach(self.driver.get_screenshot_as_png(), name = "Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Яндекс"

    @allure.feature("Open pages")
    @allure.story("Open pages Yahoo.com")
    @allure.severity("trivial")
    def test_yahoo_search(self):
        self.driver.get("https://yahoo.com")
        with allure.step("Делаем скриншот"):
            allure.attach(self.driver.get_screenshot_as_png(), name = "Screenshot", attachment_type=AttachmentType.PNG)

        assert self.driver.title == "Yahoo"

