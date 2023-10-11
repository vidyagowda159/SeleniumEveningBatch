import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element("link text", "Facebook").click()

# list of window ids opened
handles = driver.window_handles         # [Demowebshop, Facebook]
print(handles)

driver.switch_to.window(handles[1])

time.sleep(2)
driver.find_element("xpath", '//div[@aria-label="Close"]').click()
driver.find_element("name", "email").send_keys("abc@gmail.com")

# driver.close()

time.sleep(2)
driver.switch_to.window(handles[0])
driver.find_element("link text", "Register").click()

driver.quit()
