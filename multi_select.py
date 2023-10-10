import time

from selenium.webdriver.support.select import Select
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

path = r"C:\Users\Vidyashree M C\PycharmProjects\SeleniumEveningBatch\HTML_files\demo.html"
driver.get(path)
driver.maximize_window()

listbox = driver.find_element("id", "multiple_cars")

select_obj = Select(listbox)

select_obj.select_by_index(2)       # BMW
time.sleep(1)
select_obj.select_by_visible_text("Jaguar")
time.sleep(1)
select_obj.select_by_value("aud")
time.sleep(1)

# list of selected options webelement
sel_options = select_obj.all_selected_options

for option in sel_options:
	print(option.text)

# list of all the options
all_options = select_obj.options

for option in all_options:
	print(option.text)

# de-selecting
select_obj.deselect_by_index(1)
select_obj.deselect_by_value("aud")
select_obj.deselect_by_visible_text("Audi")
select_obj.deselect_all()

# is_multiple
print(select_obj.is_multiple)

# select_obj.first_selected_option
driver.close()











