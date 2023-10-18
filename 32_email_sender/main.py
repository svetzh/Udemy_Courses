# # From GMAIL to OUTLOOK

# import smtplib
#
# #  smtp.office365.com, smtp.gmail.com, smtp.mail.yahoo.com
#
# my_email = "svetinfo84@gmail.com"
# password = "rmqzzqgxxhtsloet"
#
# msg = """Subject: KURBAN
# Hello Team,
#
# I want to eat KURBAN.
#
# Best Regards
# Svet Zhelev
# """
# oYN8e#wuurju:GlW93\"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="svetin2023@outlook.com",
#         msg=msg)

## outlook_passwd = "csndfbmuakzqjrnc"
## gmail_passwd = "auemescjlmvgepfb"
## yahoo_passwd = "qomjrnfmeoemoooe"


# # # From OUTLOOK to GMAIL
# import smtplib
#
# msg = """Subject: KURBAN
# Hello FROM YAHOO,
#
# GOOD NIGHT! GOOD JOB!
#
# Best Regards
# Svet Zhelev
# """
#
#
# with smtplib.SMTP("smtp.office365.com") as connection:
#     connection.starttls()
#     connection.login(user="svetin2023@outlook.com", password='csndfbmuakzqjrnc')
#     connection.sendmail(
#         from_addr="svetin2023@outlook.com",
#         to_addrs=["svet_zh84@yahoo.com", "svetinfo84@gmail.com"],  # this list can send multiple mails
#         msg=msg)

import datetime as dt
import random
import smtplib
import requests


today = dt.datetime.now().weekday()

with open("quotes.txt", "r") as quotes_file:
    quotes = [l.strip() for l in quotes_file]

sent_email_day = 0  # since .weekday() func returns numbers 0 as Monday and 6 - Sunday, we need to set our current day
rand_quote = random.choice(quotes)

if today == sent_email_day:
    with smtplib.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(user="svetin2023@outlook.com", password="csndfbmuakzqjrnc")
        connection.sendmail(from_addr="svetin2023@outlook.com",
                            to_addrs=["svetinfo84@gmail.com", "tsonova.neli@gmail.com"],
                            msg=f'''Subject: RAND QUOTES\nHello,\n\n{rand_quote}\n\nYours\nSvetlio''')
















