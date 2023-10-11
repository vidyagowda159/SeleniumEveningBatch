import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

# # launch demowebshop url
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
#
# driver.find_element("xpath", '//input[@value="Search"]').click()
#
# # switch the control
# alert_handler = driver.switch_to.alert
#
# # accept(), dismiss(), send_keys(), text
# print(alert_handler.text)
# time.sleep(1)
# alert_handler.dismiss()
#
# # print(alert_handler.text)       # NoAlertPresentException

##################################################################################
driver.get("https://nxtgenaiacademy.com/alertandpopup/")
driver.maximize_window()

# simple alert
driver.find_element("name", "alertbox").click()
time.sleep(2)
alert_obj = driver.switch_to.alert
alert_obj.accept()
# alert_obj.dismiss()

# confirmation alert
driver.find_element("name", "confirmalertbox").click()

alert_obj = driver.switch_to.alert
time.sleep(2)
# alert_obj.accept()
alert_obj.dismiss()

# prompt alerts
driver.find_element("name", "promptalertbox1234").click()

alert_obj = driver.switch_to.alert
time.sleep(2)

alert_obj.send_keys("no")
alert_obj.accept()
# alert_obj.dismiss()


