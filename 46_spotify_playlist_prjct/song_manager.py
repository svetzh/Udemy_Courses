import datetime as dt
import requests
from bs4 import BeautifulSoup


class Top100:
    def __init__(self):
        self.base_url = "https://www.billboard.com/charts/hot-100/"
        self.date = None
        self.year = None
        self.month = None
        self.day = None

    def pick_date(self):
        if self.date:
            return self.date, self.year, self.month, self.date
        while True:
            print('Which year do you want to travel to? Type the date in this format YYYY-MM-DD')
            try:
                year = int(input('Year (YYYY): '))
                month = int(input('Month (1-12): '))
                day = int(input('Day (1-31): '))

                if not (0 < year <= dt.datetime.now().year and 0 < month <= 12 and 0 < day <= 31):
                    print("Invalid input. Please enter valid values for year, month, and day.")
                    continue

                last_day = (dt.date(year, month % 12 + 1, 1) - dt.timedelta(days=1)).day
                if not (0 < day <= last_day):
                    print(f"Invalid day for {dt.date(year, month, 1).strftime('%B %Y')}.")
                    continue

                date = dt.date(year, month, day)
                self.date = date
                self.year = year
                self.month = month
                self.day = day
                return date, year, month, day

            except ValueError:
                print("Invalid date. Please try again.")

    def songs(self):
        try:
            date = self.pick_date()[0]
            url = f'{self.base_url}{date}'
            response = requests.get(url)
            response.raise_for_status()  # Check for request errors
            soup = BeautifulSoup(response.text, "html.parser")
            song_names = [song.get_text(strip=True) for song in soup.select('li ul li h3')]
            return song_names
        except requests.exceptions.HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except requests.exceptions.RequestException as request_exception:
            print(f"Request error occurred: {request_exception}")
