import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    to_alert_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    to_alert_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x_text = x_element.text
    answer = calc(x_text)

    answer_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_field.send_keys(answer)

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
