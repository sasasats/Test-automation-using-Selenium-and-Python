import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

text_field_template = "//input[@name='{}']"
link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
try:
    browser.get(link)
    first_name_field = browser.find_element(By.XPATH, text_field_template.format('firstname'))
    first_name_field.send_keys('First name')
    last_name_field = browser.find_element(By.XPATH, text_field_template.format('lastname'))
    last_name_field.send_keys('Last name')
    email_field = browser.find_element(By.XPATH, text_field_template.format('email'))
    email_field.send_keys('Email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    choose_file_button = browser.find_element(By.CSS_SELECTOR, '#file')
    choose_file_button.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
