from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # for making a service obj from exec path
from selenium.webdriver.support.ui import WebDriverWait  # for using explict wait
from selenium.webdriver.support import expected_conditions as ec  # to specify the condition to wait by
from selenium.webdriver.common.by import By  # to find elements By (id,class etc)
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time_table import time_table
import time
from datetime import datetime as dt
from dotenv import load_dotenv
from os import getenv

load_dotenv()
Website = f'{getenv("CLASSES_WEBSITE")}'
user_id = f'{getenv("USER_ID")}'
password = f'{getenv("PASSWORD")}'

# getting the current time and weekday
today = dt.today().strftime("%A %I %M").split()
weekday,curr_hour,curr_min = today
today_time_table = time_table[weekday]
print(weekday,curr_hour,curr_min)
print(time_table[weekday])

op = Options()
op.add_argument("user-data-dir=/home/rudra/.config/google-chrome")
op.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
})
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
driver.get(f"{Website}")
driver.maximize_window()
try:
    element = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, "button-1")))
    # webdriver waits for 5 seconds until the condition (presence of ele located is fullfilled)
    # then it moves on and find element by class name ,id , or css selectors etc
    agree_button = driver.find_element(by=By.CLASS_NAME, value="button-1")
    agree_button.click()
    user_id_input = driver.find_element(by=By.ID, value="user_id")
    user_id_input.send_keys(user_id)
    password_input = driver.find_element(by=By.ID, value="password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    # getting the class link from time table
    for ele in today_time_table:
        curr_class,st_time_hour,st_time_min = today_time_table[ele]
        if st_time_hour==curr_hour and st_time_min-5 < curr_min <st_time_min+5:
            driver.get(curr_class)
            break
        else:
            print("No classes found")

    drop_down_ele = WebDriverWait(driver, 9).until(ec.element_to_be_clickable((By.ID, "sessions-list-dropdown")))
    # time.sleep(5)
    join_session_drop_down = driver.find_element(by=By.ID, value="sessions-list-dropdown")
    join_session_drop_down.click()
    join_button = driver.find_element(by=By.XPATH, value='//*[@id="sessions-list"]/li/a')
    join_button.click()
except TimeoutException as E:
    print('Failed')
time.sleep(100)
driver.close()
