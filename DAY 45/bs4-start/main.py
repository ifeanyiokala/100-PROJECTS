# from turtle import heading
# from bs4 import BeautifulSoup

# # import lxml

# with open("website.html",encoding="utf8") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, "html.parser")



# # print(soup.title)
# # print(soup.title.string)

# # print(soup.prettify())

# # print(soup.a)

# # all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))




# # heading = soup.find(name='h1', id="name")
# # print(heading)


# section_heading = soup.find(name='h3', class_="heading")
# print(section_heading.get("class"))


# name  = soup.select_one(selector="#name")

# print(name)


# headings = soup.select(".heading")
# print(headings)

from gettext import gettext
from webbrowser import get
from bs4 import BeautifulSoup
from numpy import number
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.title)

heading = soup.find_all(name='a', class_="titlelink")

articles_texts = []
article_links = []



for article in heading:
    text = article.getText()
    articles_texts.append(text)
    link =  article.get("href")
    article_links.append(link)




article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_value = max(article_upvote)
print(max_value)

max_index = article_upvote.index(max_value)
print(max_index)




print(articles_texts[max_index])
print(article_links[max_index])
print(article_upvote[max_index])
























