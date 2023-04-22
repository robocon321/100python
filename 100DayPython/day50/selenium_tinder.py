from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = 'D:\Software\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url = 'https://tinder.com/')

sleep(4)

create_account_btn = driver.find_element('xpath', '//*[@id="q554704800"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
create_account_btn.click()

login_gg_btn = driver.find_element('xpath', '//*[@id="q-1173676276"]/div/div/div[1]/div/div/div[3]/span/div/div/button')
login_gg_btn.click()

sleep(2)
email_input = driver.find_element('css selector', 'input[type="email"]')
