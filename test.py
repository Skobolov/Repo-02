link = 'https://www.google.com/'

def test_title_1(brChrome):
    brChrome.get(link)
    assert "Google" in brChrome.title

def test_title_2(brChrome):
    brChrome.get(link)
    assert "Gogle" in brChrome.title

