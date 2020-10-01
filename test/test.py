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

print("aaaaaaaaa")
