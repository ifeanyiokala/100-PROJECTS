from turtle import heading
from bs4 import BeautifulSoup

# import lxml

with open("website.html",encoding="utf8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")



# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))




# heading = soup.find(name='h1', id="name")
# print(heading)


section_heading = soup.find(name='h3', class_="heading")
print(section_heading.get("class"))


name  = soup.select_one(selector="#name")

print(name)


headings = soup.select(".heading")
print(headings)















