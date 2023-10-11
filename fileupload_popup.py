from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element("xpath", '//div[contains(text(), "Upload Resume")]').click()
file_path = r"C:\Users\Vidyashree M C\PycharmProjects\SeleniumEveningBatch\notes\basics.txt"
driver.find_element("name", "file").send_keys(file_path)

