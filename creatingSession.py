# pip install selenium
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

# creating webdriver
driver = webdriver.Chrome(options=opts)     # create chrome session
print(driver)

#-------------------------------------------------------------------
from selenium import webdriver

driver = webdriver.Firefox()
print(driver)












