from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'D:\Software\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url = 'https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element("name", "fName")
last_name = driver.find_element("name", "lName")
email = driver.find_element("name", "email")
submit = driver.find_element("tag name", "button")

first_name.send_keys("Nhat")
last_name.send_keys("Nguyen")
email.send_keys("robocon321n@gmail.com")
submit.click()