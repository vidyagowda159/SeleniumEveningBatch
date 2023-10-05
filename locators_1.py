import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# # locating search bar using name locator
# search_bar = driver.find_element("name", "q")
# search_bar.send_keys("Books")

# # locating search bar using class name locator
# search_bar = driver.find_element("class name", "search-box-text.ui-autocomplete-input")
# search_bar.send_keys("Books")

# locating using link text locator
# driver.find_element("link text", 'Register').click()
# driver.find_element("link text", "Log in").click()

# driver.find_element("partial link text", "Reg").click()
driver.find_element("partial link text", "Books").click()


