from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", rel="noreferrer")

article_texts = []
article_links = []

for tag in articles:
    text = tag.get_text()
    article_texts.append(text)

    link = tag.get("href")
    article_links.append(link)


article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
largets_num = max(article_upvotes)
largets_index = article_upvotes.index(largets_num)

print(article_texts[largets_index])
print(article_links[largets_index])
print(article_upvotes[largets_index])


# sorted_lists = sorted(zip(article_texts, article_links, article_upvotes), key=lambda x: -x[2])
# print(sorted_lists)
