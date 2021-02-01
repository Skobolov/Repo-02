link = 'https://www.google.com/'

def test_title_1(driver):
    driver.get(link)
    assert "Google" in driver.title

def test_title_2(brChrome):
    brChrome.get(link)
    assert "Gogle" in brChrome.title

