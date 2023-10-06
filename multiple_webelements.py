# find_element() --> single webelement
# find_elements() --> return list of webelements

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

path = r"C:\Users\Vidyashree M C\Desktop\Documents\HTML files\demo.html"
driver.get(path)
driver.maximize_window()

# links = driver.find_elements("xpath", "//a")

links = driver.find_elements("tag name", "a")

for link in links:
	print(link.text)
	print(link.get_attribute("href"))

######################################################################

checkboxes = driver.find_elements("xpath", '//input[@name="download"]')

for checkbox in checkboxes:
	checkbox.click()
	time.sleep(1)

#######################################################################
# python.org --> links with "python" in their text --> capture text and also href

# https://www.python.org/downloads/ --> click on download link of python 3.11.5

