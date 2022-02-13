from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # for making a service obj from exec path
from selenium.webdriver.support.ui import WebDriverWait  # for using explict wait
from selenium.webdriver.support import expected_conditions as EC  # to specify the condition to wait by
from selenium.webdriver.common.by import By  # to find elements By (id,class etc)
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
from os import getenv

load_dotenv()
CHROMEDRIVER_EXEC_PATH = Service(f'{getenv("CHROME_DRIVER_PATH")}')
Website = f'{getenv("CLASSES_WEBSITE")}'
user_id = f'{getenv("USER_ID")}'
password = f'{getenv("PASSWORD")}'

driver = webdriver.Chrome(service=CHROMEDRIVER_EXEC_PATH)
driver.get(f"{Website}")
driver.maximize_window()
try:
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "button-1")))
    # webdriver waits for 5 seconds until the condition (presence of ele located is fullfilled)
    # then it moves on and find element by class name ,id , or css selectors etc
    agree_button = driver.find_element(by=By.CLASS_NAME, value="button-1")
    agree_button.click()
    user_id_input = driver.find_element(by=By.ID, value="user_id")
    user_id_input.send_keys(user_id)
    password_input = driver.find_element(by=By.ID,value="password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
except TimeoutException as E:
    print('Failed')
time.sleep(100)
driver.close()
