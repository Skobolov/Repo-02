import pytest

link = 'https://www.google.com/'

def test_title_1(browser):
    browser.get(link)
    assert "Google" in browser.title

@pytest.mark.xfail
def test_title_2(browser):
    browser.get(link)
    assert "Gogle" in browser.title