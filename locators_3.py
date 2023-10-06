"""
css - tagname[attr_name=attr_value]

types of xpath
1. absolute xpath(/ - immediate child): root tag
2. relative xpath(// - any child): any tag

# xpath using attributes:   //tagname[@attr_name=attr_value]

# xpath using text: //tagname[text()=value]

# xpath using group indexing: (xpath_expression)[index]   --> index starts from 1

# xpath using contains():

	//tagname[contains(@attr_name, partial_attr_value)]

	//tagname[contains(text(), partial_text)]

# dependent independent xpath
- locate dynamically changing elements
- handle web tables

name    marks
john    45
steve   20



"""
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# driver.find_element("xpath", '//input[@value="Search store"]').send_keys("Mobiles")
# time.sleep(2)
#
# driver.find_element("xpath", '//input[@type="submit"]').click()
# time.sleep(2)
#
# driver.find_element("xpath", '//a[text()="Register"]').click()

###########################################################################

# driver.find_element("xpath", '(//a[contains(text(), "Books")])[1]').click()

# -------------------------------------------------------------------------















