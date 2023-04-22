from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'D:\Software\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url = 'https://en.wikipedia.org/wiki/Main_Page')

# total = driver.find_element("css selector", "#articlecount a:nth-child(1)")
# total.click()

search = driver.find_element("name", "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)