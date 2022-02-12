from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from dotenv import load_dotenv
from os import getenv

load_dotenv()
CHROMEDRIVER_EXEC_PATH = Service(f'{getenv("CHROME_DRIVER_PATH")}')

driver = webdriver.Chrome(service=CHROMEDRIVER_EXEC_PATH)
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(5)
driver.close()