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

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button = driver.find_element_by_id("book")
button.click()


x_element = driver.find_element_by_id("input_value")
driver.execute_script("return arguments[0].scrollIntoView(true);", x_element)
x = x_element.text
y = calc(x)

input1 = driver.find_element_by_id("answer")
driver.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)


button2 = driver.find_element_by_id("solve")
button2.click()

time.sleep(5)
driver.quit()