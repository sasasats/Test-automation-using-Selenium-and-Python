import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'https://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()
try:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    num1_text = x_element.text
    answer = calc(num1_text)

    answer_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(answer)

    i_am_the_robot_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    i_am_the_robot_checkbox.click()

    robots_rule_radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots_rule_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()