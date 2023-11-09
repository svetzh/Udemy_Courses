from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")

items_ids = [item.get_attribute("id") for item in items]

five_seconds = time.time() + 5
five_minute = time.time() + (60 * 5)

while True:
    cookie.click()
    if time.time() > five_seconds:

        all_price = driver.find_elements(By.CSS_SELECTOR, '#store b')
        item_prices = []

        for price in all_price:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)


        cookie_upgrade = {}

        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = items_ids[n]

        money_element = driver.find_element(By.ID, "money").text

        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)

        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.CSS_SELECTOR, f"#{to_purchase_id}").click()

        five_seconds = time.time() + 5

    if time.time() > five_minute:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break






