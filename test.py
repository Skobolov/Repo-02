
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https://google.com")
assert driver.title == "Google"
time.sleep(20)
driver.quit()

