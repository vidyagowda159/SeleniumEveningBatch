"""
1. identify dependent and independent element
2. locate independent element
3. move backward till the common parent of both dep and indep element
4. locate dependent element

"""

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# path = r"C:\Users\Vidyashree M C\Desktop\Documents\HTML files\demo.html"
# driver.get(path)
# driver.maximize_window()
#
# # driver.find_element("xpath", '//td[text()="Perl"]/..//input[@name="download"]').click()
#
# # time.sleep(5)
# price = driver.find_element("xpath", '//td[text()="FB"]/..//td[@class="price"]').text
# print(price)

#--------------------------------------------------------------------------------
driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
driver.maximize_window()
time.sleep(5)
share_price = driver.find_element("xpath", '(//a[text()="BAJAJFINSV"]/../..//td)[7]').text
print(share_price)
