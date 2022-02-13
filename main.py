from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
from os import getenv

load_dotenv()
CHROMEDRIVER_EXEC_PATH = Service(f'{getenv("CHROME_DRIVER_PATH")}')
Website = f'{getenv("CLASSES_WEBSITE")}'

driver = webdriver.Chrome(service=CHROMEDRIVER_EXEC_PATH)
driver.get(f"{Website}")
driver.maximize_window()
try:
    element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"button-1")))
    agree_button = driver.find_element(by=By.CLASS_NAME,value="button-1")
    agree_button.click()
except Exception as E:
    print('Failed')
time.sleep(100)
driver.close()
