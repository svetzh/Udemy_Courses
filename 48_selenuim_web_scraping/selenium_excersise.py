from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/svetl/Documents/Development/chromedriver.exe"  # exact path to the browser driver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li a")

events_dict = {}

# for n in range(len(event_times)):
#     event_date_full = event_times[n].get_attribute("datetime")
#     event_date = event_date_full[:10]
#     event_name = event_elements[n].text
#     events_dict[n] = {
#         "time": event_date,
#         "name": event_name,
#     }

for n, (event_time, event_element) in enumerate(zip(event_times, event_elements)):
    event_date_full = event_time.get_attribute("datetime")
    event_date = event_date_full[:10]
    event_name = event_element.text
    events_dict[n] = {
        "time": event_date,
        "name": event_name,
    }


print(events_dict)

# driver.quit()