from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/svetl/Documents/Development/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/")

article_numbers = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
print(article_numbers)
