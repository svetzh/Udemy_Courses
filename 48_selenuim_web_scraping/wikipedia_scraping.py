from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = "/Users/svetl/Documents/Development/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Wikipedia")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# content_portals_link = driver.find_element(By.XPATH, "//a[@title='Wikipedia:Contents/Portals']")
#
# # Click the "Content portals" link
# content_portals_link.click()


wait = WebDriverWait(driver, 10)
search = wait.until(EC.visibility_of_element_located((By.NAME, "search")))

search.send_keys("Python")
search.submit()

input()



