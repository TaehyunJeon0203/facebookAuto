from selenium import webdriver
from selenium.webdriver.common.by import by

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://google.co.kr")


input()