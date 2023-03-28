# python3 -m pip install requests

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://peri.io/metrotown'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Find all radio button elements on the page
radio_buttons = soup.find_all('input', {'type': 'radio'})


response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# target_label = ['No', 'Take Out', 'Excellent', '10']
target_label = [ 'Take Out', 'Excellent', '10']

driver = webdriver.Chrome()

value_list = []
for radio_button in radio_buttons:
    # print(">>>", radio_button.next_sibling.next_sibling.text.strip())
    if radio_button.next_sibling.next_sibling.text.strip() in target_label:
        print(radio_button.next_sibling.next_sibling.text.strip() , " : ", radio_button['value'])
        driver.get(url)
        radio_button_value = radio_button['value']
        value_list.append(radio_button_value)
        # select_button = driver.find_element(By.XPATH, f'//input[@type="radio" and @value="{radio_button_value}"]')
        # radio_button.click()
count = 0
for radio_button_value in value_list:
    radio_button = driver.find_element(By.XPATH, f'//input[@type="radio" and @value="{radio_button_value}"]')
    radio_button.click()

    # driver.refresh()

submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_button.click()

response = driver.page_source
if "Form submitted successfully!" in response:
    print('Form submitted successfuly!')
else:
    print('Form submission failed. check for any unchecked boxes')
time.sleep(100)
driver.quit()
