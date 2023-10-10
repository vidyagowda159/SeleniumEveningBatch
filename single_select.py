import time

from selenium.webdriver.support.select import Select
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

path = r"C:\Users\Vidyashree M C\PycharmProjects\SeleniumEveningBatch\HTML_files\demo.html"
driver.get(path)
driver.maximize_window()

# locate listbox
listbox = driver.find_element("id", "standard_cars")

# instantiate select class
select_obj = Select(listbox)
time.sleep(2)

# selecting an option
select_obj.select_by_visible_text("BMW")
print(select_obj.first_selected_option.text)
time.sleep(1)

select_obj.select_by_value("jgr")
print(select_obj.first_selected_option.text)
time.sleep(1)

select_obj.select_by_index(1)
# first_selected_option --> current selected option
print(select_obj.first_selected_option.text)

# list of options
all_options = select_obj.options

for option in all_options:      # option -> webelement
	print(option.text)

# is_multiple
print(select_obj.is_multiple)

driver.close()





