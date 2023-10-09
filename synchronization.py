import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

path = r"C:\Users\Vidyashree M C\Desktop\Documents\HTML files\loading.html"

driver.get(path)
driver.maximize_window()

# # unconditional synchronization
# time.sleep(15)
# driver.find_element("name", "fname").send_keys("Steve")

# conditional synchronization
# # 1. implicit wait - find_element & find_elements()
#
# driver.implicitly_wait(15)
# driver.find_element("name", "fname").send_keys("Steve")

# 2. explicit wait - accepts external conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# wait object
wait_ = WebDriverWait(driver, 5)

# specify the condition to wait for
locator = ("name", "fname")

element = wait_.until(ec.visibility_of_element_located(locator), message="Element not visible")
element.send_keys("steve")
# driver.find_element("name", "fname").send_keys("Steve")

# element = driver.find_element("name", "fname")
# wait_.until(ec.visibility_of(element))

# ----------------------------------------------------------------------------------
# wait until the loading symbol becomes invisible
# progressbar.html -> wait until the bar reaches 100% and click the button once again







