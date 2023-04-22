from selenium import webdriver

chrome_driver_path = 'D:\Software\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com/Carhartt-Mens-NWP-M-Brown-Tanned/dp/B00TR3KZF6/ref=sr_1_1_sspa?crid=JYMRM6EUX8O5&keywords=shoe&qid=1660004137&sprefix=sh%2Caps%2C366&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzU1Q0WDJaRUI3NzI0JmVuY3J5cHRlZElkPUEwNjcxNzYyMTczNEsyWTNHMzNVVyZlbmNyeXB0ZWRBZElkPUEwODEzOTAxMjhPTEI4UVoyTDg2ViZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")

title = driver.find_elements("css selector", "p")
print(len(title))

