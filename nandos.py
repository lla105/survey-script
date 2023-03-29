# python3 -m pip install requests

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

url = 'http://peri.io/metrotown'
# url = 'https://docs.google.com/forms/d/e/1FAIpQLSeB35vJidVD3GneKC7MO63NQYKTslhlqMvi8QheWKV7_A1R-Q/viewform?vc=0&c=0&w=1&flr=0'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Find all radio button elements on the page
radio_buttons = soup.find_all('input', {'type': 'radio'})


# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
target_label = ['No', 'Take Out', 'Excellent', '10']
# target_label = [ 'Take Out', 'Excellent', '10']

driver = webdriver.Chrome()

value_list = []
for radio_button in radio_buttons:
    if radio_button.next_sibling.next_sibling.text.strip() in target_label:
        print(radio_button.next_sibling.next_sibling.text.strip() , " : ", radio_button['value'])
        driver.get(url)
        radio_button_value = radio_button['value']
        value_list.append(radio_button_value)

count = 0
try:
    for radio_button_value in value_list:
        radio_button = driver.find_element(By.XPATH, f'//input[@type="radio" and @value="{radio_button_value}"]')
        radio_button.click()
except NoSuchElementException:
    print("Text input nto found. Skipping...")
    # driver.refresh()

# Find text input field by IA. Fill in text.
try : 
    text_input = driver.find_element(By.CLASS_NAME, 'textarea')
    text_input.send_keys("nando's chicken was so good it saved my failing marriage and cured my crippling depression")
except NoSuchElementException:
    print("Text input nto found. Skipping...")

try:
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    # submit_button.click()
except NoSuchElementException:
    print("Text input nto found. Skipping...")


response = driver.page_source
if "Form submitted successfully!" in response:
    print('Form submitted successfuly!')
else:
    print('Form submission failed. check for any unchecked boxes')

time.sleep(100)
driver.quit()
