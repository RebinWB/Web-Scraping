import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = ""  # Enter your Browser Driver Path

driver = webdriver.Firefox(executable_path=PATH)  # Based on Your Browser Change it
driver.get("https://github.com")  # Go to Github

login_link = driver.find_element(by=By.LINK_TEXT, value="Sign in")  
login_link.click()

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "auth-form-body"))
    )

    username_field = main.find_element(by=By.ID, value="login_field")
    username_field.send_keys("")  # Enter Your Github Username
    password_field = main.find_element(by=By.ID, value="password")
    password_field.send_keys("")  # Enter Your Github Password 

    submit = main.find_element(by=By.NAME, value="commit")
    submit.click()

except:
    driver.quit()

finally:
    """
    Wait for 10 Seconds and Close the Browser
    """
    time.sleep(10)
    driver.quit()



