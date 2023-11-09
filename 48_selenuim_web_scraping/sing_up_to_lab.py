from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "/Users/svetl/Documents/Development/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get('http://secure-retreat-92358.herokuapp.com/')

wait = WebDriverWait(driver, 8)

f_name = wait.until(EC.visibility_of_element_located((By.NAME, "fName")))
f_name.send_keys("Svet")

l_name = wait.until(EC.visibility_of_element_located((By.NAME, "lName")))
l_name.send_keys("Zhelev")

mail = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
mail.send_keys("svzh@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, "form button")

button.click()
input()