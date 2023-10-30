import time
import smtplib
import random

# Define the time at which you want to send the email (e.g., 14:00)
desired_time = "14:00"

# Function to send the email
def send_email():
    # Your email sending logic here
    rand_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(user="svetin2023@outlook.com", password="csndfbmuakzqjrnc")
        connection.sendmail(from_addr="svetin2023@outlook.com",
                            to_addrs=["svetinfo84@gmail.com", "tsonova.neli@gmail.com"],
                            msg=f"Subject: RAND QUOTES\nHello,\n\n{rand_quote}\n\nYours\nSvetlio")

# Load your list of quotes from a file (assuming quotes.txt)
with open("quotes.txt", "r") as quotes_file:
    quotes = [line.strip() for line in quotes_file]

while True:
    current_time = time.strftime("%H:%M")

    if current_time == desired_time:
        send_email()

    # Adjust the sleep interval to avoid excessive CPU usage
    time.sleep(60)
