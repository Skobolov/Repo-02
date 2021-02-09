import pytest
import allure

link = 'https://www.google.com/'

@allure.feature("Open pages Google")
@allure.story("Открываем страницу google.com")
@allure.severity("blocker")
def test_title_3(browser):
    browser.get(link)
    assert "Google" in browser.title

@allure.feature("Open pages Google_2")
@allure.story("Открываем страницу google.com")
@allure.severity("blocker")
@pytest.mark.xfail
def test_title_4(browser):
    browser.get(link)
    assert "Gogle" in browser.title