import pandas as pd
from datetime import datetime as dt
import smtplib
from random import randint

today = dt.now()
current_date = (today.month, today.day)
info_file = pd.read_csv("birthdays.csv")
bday_dict = {(value["month"], value["day"]): value for (key, value) in info_file.iterrows()}
dir_path = f"letter_templates/letter_{randint(1, 3)}.txt"

if current_date in bday_dict:
    name_person = bday_dict[current_date]
    with open(dir_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", name_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="svetinfo84@gmail.com", password="auemescjlmvgepfb")
        connection.sendmail(from_addr="svetinfo84@gmail.com",
                            to_addrs="svetin2023@outlook.com",
                            msg=f"Subject: Happy B-DAY!\n\n{contents}")

