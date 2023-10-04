import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# find the search bar element
result = driver.find_element("id", "small-searchterms")
print(result)

# webelement methods
# result.click()
result.send_keys("books")
time.sleep(2)
result.clear()

# # position and size
# print(result.location)
# print(result.size)
# print(result.rect)

# print(result.is_enabled())
# print(result.is_displayed())
# print(result.is_selected())     # radio buttons, checkboxes

print(result.get_attribute("role"))     # returns attribute value of attr name specified

driver.close()
