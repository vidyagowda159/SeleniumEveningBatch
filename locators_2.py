# CSS selector - to locate elements using any attributes
# syntax: tagname[attr_name = attr_value]


from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# driver.find_element("css selector", 'input[value="Search"]').click()

driver.find_element("css selector", 'form[novalidate="novalidate"]>input[value="Search store"]').send_keys("books")

"""
drawbacks
---------
1. indexing is not possible
2. doesnot support backward traversal(child to parent)
3. cannot locate an element using its text
"""