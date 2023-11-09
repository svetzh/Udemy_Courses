import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "svetinfo84@gmail.com"
password = "urcvwefrsaoafqcm "

def check_price():

    # smtp.gmail.com -> server address for Gmail

    url = "https://www.amazon.com/Xiaomi-Factory-Unlocked-International-Version/dp/B0BT8KR6W2/ref=sr_1_2?crid=1JFHG9O6Y7UGU&keywords=xiaomi%2Bpoco%2Bf5%2Bpro&qid=1699357473&refinements=p_n_feature_seventeen_browse-bin%3A23488163011%7C23488164011%2Cp_n_feature_thirty-nine_browse-bin%3A113334730011%2Cp_n_feature_thirty-two_browse-bin%3A108501313011&rnid=25926948011&s=wireless&sprefix=xiaomi%2Bpok%2Caps%2C184&sr=1-2&th=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept-Language": "en-US,en;q=0.5"
    }
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    webpage = response.text

    soup = BeautifulSoup(webpage, "html.parser")

    price_tag = float(soup.find(name="span", class_="a-price-whole").get_text())

    if price_tag is None:
        return None
    else:
        return price_tag


link = "https://www.amazon.com/Xiaomi-Factory-Unlocked-International-Version/dp/B0BT8KR6W2"

get_current_price = check_price()

if get_current_price < 250.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="svetin2023@outlook.com",
            msg=f'''Subject: GOOD DEAL\nHello,\n\nORDER NOW! Follow link: {link}\n\nYours\nSvetlio''')


