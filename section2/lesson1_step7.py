import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
try:
    browser.get(link)
    treasure_chest_image = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = treasure_chest_image.get_attribute('valuex')
    y = calc(x)
    answer_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_field.send_keys(y)
    i_am_the_robot_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    i_am_the_robot_checkbox.click()
    robots_rule_radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots_rule_radiobutton.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
