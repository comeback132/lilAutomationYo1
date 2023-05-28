from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver')

chrome_browser = webdriver.Chrome(service=service)

chrome_browser.maximize_window()
chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

#assert checks whether the statement is True/False and would give an error or run
assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message=chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOL')

show_message_button.click()
output_message=chrome_browser.find_element(By.ID, 'display')

chrome_browser.close()


while True:
    pass

