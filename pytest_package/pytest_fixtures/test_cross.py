import time

import pytest
from selenium import webdriver


@pytest.fixture(params=["firefox", "chrome"])
def driver_init(request):
	browser = request.param

	if browser == "chrome":
		opts = webdriver.ChromeOptions()
		opts.add_experimental_option("detach", True)
		driver = webdriver.Chrome(options=opts)

	elif browser == "firefox":
		driver = webdriver.Firefox()

	driver.get("https://demo.actitime.com/login.do")
	driver.maximize_window()
	yield driver
	driver.close()


def test_login(driver_init):
	driver = driver_init
	driver.find_element("id", "username").send_keys("admin")
	time.sleep(1)
	driver.find_element("name", "pwd").send_keys("manager")
	time.sleep(1)
	driver.find_element("xpath", '//div[text()="Login "]').click()
	time.sleep(1)

