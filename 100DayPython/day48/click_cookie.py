from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'D:\Software\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url = 'http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element("id", "cookie")
for i in range(50):
    cookie.click()
