import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(number1, number2):
    return int(number1) + int(number2)


link = 'https://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
try:
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num1_text = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    num2_text = num2.text
    answer = calc(num1_text, num2_text)

    answer_dropdown = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    answer_dropdown.select_by_value(str(answer))

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
