# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# #Keep Chorme browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Xiaomi-Factory-Unlocked-International-Version/dp/B0BT8KR6W2?th=1")
#
# price_dollar = driver.find_element(By.CLASS_NAME, 'class="a-price-whole"')
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
#
# # driver.close()  # -> closes a tab
# driver.quit()  # -> closes entire window


# # Keeps Firefox browser open
# from selenium import webdriver
#
# # Initialize the Firefox WebDriver
# driver = webdriver.Firefox()
#
# # Open a website
# driver.get("https://www.amazon.com")

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Xiaomi-Factory-Unlocked-International-Version/dp/B0BT8KR6W2?th=1")
driver.get("https://www.python.org/")

# Use a CSS selector to locate elements
# price_dollar = driver.find_element(By.CSS_SELECTOR, '.a-price-whole')
# price_cents = driver.find_element(By.CSS_SELECTOR, '.a-price-fraction')
# print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, "submit")
print(button.size)
document_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(document_link.text)

# # if nothing else works XPATH should always work
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)



# driver.close()  # -> closes a tab
# driver.quit()  # -> closes the entire window










