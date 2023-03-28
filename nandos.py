# python3 -m pip install requests

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new webdriver instance using chromedriver
driver = webdriver.Chrome()


url = 'http://peri.io/metrotown'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Find the radio button element by its value attribute
radio_button = soup.find('input', {'type': 'radio', 'value': '3695211913'})
# Find all radio button elements on the page
radio_buttons = soup.find_all('input', {'type': 'radio'})
# Extract values of all radio buttons and store them in a list
radio_button_values = [rb['value'] for rb in radio_buttons]
print(radio_button_values)


payload = {'option': radio_button['value'] }
radio_button_value = radio_button['value']
# Open webpage using Selenium
driver = webdriver.Chrome()
driver.get(url)
#Find radio button element by its value and click it
radio_button = driver.find_element(By.XPATH, f'//input[@type="radio" and @value="{radio_button_value}"]')
radio_button.click()

# driver.refresh()

response = requests.post(url, data=payload)

if response.status_code == 200:
    print('Form submitted successfully!')
else:
    print('Form submission failed.')
  
# Get the value of the radio button
# radio_button_value = radio_button['value']
# print(radio_button_value)  # Output: option1

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
target_label = ['No', 'Take Out', 'Excellent', '10']
for radio_button in radio_buttons:
    # print(">>>", radio_button.next_sibling.next_sibling.text.strip())
    if target_label in radio_button.next_sibling.next_sibling.text.strip() :
        print(target_label)
    # if target_label in radio_button.next_sibling.strip():
    #     print("Radio button value:", radio_button['value'])
    #     break

time.sleep(10)
driver.quit()
