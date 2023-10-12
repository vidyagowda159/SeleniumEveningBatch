import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

path = r"C:\Users\Vidyashree M C\PycharmProjects\SeleniumEveningBatch\HTML_files\iframe.html"
driver.get(path)
driver.maximize_window()
driver.implicitly_wait(5)

# # using index
# driver.switch_to.frame(0)

# # using id attribute
# driver.switch_to.frame("FR1")

# using name attribute
# driver.switch_to.frame("frame1")

# using frame webelement
iframe_element = driver.find_element("xpath", '//iframe[@name="frame1"]')
driver.switch_to.frame(iframe_element)

driver.find_element("id", "small-searchterms").send_keys("mobiles")

# # switch to parent frame
# driver.switch_to.parent_frame()

# switch to root page
driver.switch_to.default_content()

# switching to second frame
driver.switch_to.frame("FR2")

driver.find_element("id", 'search_form').send_keys("vehicle insurance")

"""
parent
	frame1
		frame2
	
	frame3
		frame4
			frame5

"""