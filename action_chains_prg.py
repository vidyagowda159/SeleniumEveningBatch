import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

action_obj = ActionChains(driver)

driver.get("https://www.nykaa.com/")
driver.maximize_window()

accessories = driver.find_element("xpath", '//a[text()="appliances"]')

action_obj.move_to_element(accessories).perform()
action_obj.context_click(accessories).perform()

############################################################
path = r"C:\Users\Vidyashree M C\Desktop\Documents\HTML files\actions.html"
driver.get(path)
driver.maximize_window()

first_input = driver.find_element("id", "clickField")

action = ActionChains(driver)

# single click on first input
action.click(first_input).perform()

# double click on first input
action.double_click(first_input).perform()

# context click on first input
action.context_click(first_input).perform()

########################################################################
# drag and drop

driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
driver.maximize_window()

source = driver.find_element("id", "draggable")
target = driver.find_element("id", "droppable")

action_obj.drag_and_drop(source, target).perform()

#######################################################################
# performing page down operation
time.sleep(2)
action_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
action_obj.send_keys(Keys.PAGE_UP).perform()

# control + a
action_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# action_obj.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()








