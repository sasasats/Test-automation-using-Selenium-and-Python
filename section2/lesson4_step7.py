import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    price_element = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

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
