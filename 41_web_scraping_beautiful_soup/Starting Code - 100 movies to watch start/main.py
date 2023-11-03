import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_movie_site = response.text

soup = BeautifulSoup(empire_movie_site, "html.parser")
top_100 = soup.find_all(name="h3", class_="title")


movie_titles = [movie.get_text() for movie in top_100]
reversed_movies_list = movie_titles[::-1]

with open("movies.txt", "w") as file:
    for movie in reversed_movies_list:
        file.write(f"{movie}\n")

print("Movies created in 'movies.txt'")
