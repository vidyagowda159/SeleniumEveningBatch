# driver methods
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

# launch demowebshop url
driver.get("https://demowebshop.tricentis.com/")

# maximize window
driver.maximize_window()
time.sleep(2)

driver.minimize_window()
time.sleep(2)

driver.fullscreen_window()

# navigation
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

# position and size of the window
print(driver.get_window_position())     # {x: , y: }
print(driver.get_window_size())         # {width: , height: }
print(driver.get_window_rect())         # {width: , height: , x: , y: }

# properties of the window
print(driver.current_url)
print(driver.title)
print(driver.name)      # browser name

# close the window
# driver.close()      # closes the currently active window

driver.quit()           # close the entire session





