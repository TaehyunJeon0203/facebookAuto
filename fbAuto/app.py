from selenium import webdriver
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://business.facebook.com/latest/content_calendar?asset_id=375188782338191")

input()