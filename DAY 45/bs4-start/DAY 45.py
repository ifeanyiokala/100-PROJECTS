# request the url 
# find the tag 
# print it out 
#run it throgh a for loop
#print them out in a list with their numbers
# reorder their number 
# save it all in a text file

# IMPORTED THE NEEDED MODULES
from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text

stew = BeautifulSoup(web_page,"html.parser")

# SEARCHED FOR THE SPECIFIC TAG I NEEDED
heading = stew.find_all('h3','title')


# for article in heading:
#RAN A FOR LOOP FOR EACH TAG AND 
# STORED IT IN A STRING USING LIST COMPREHENSION
name = [article.getText() for article in heading]
articles_new = name[::-1]

# print(articles_new)
    # print(name)
    # new = name.split(")")
    # articles_text.append(new)
     
# print(articles_new.count())
# for i in range(100):
#     print(articles_new[i][0])
#     print(articles_new[i][1])

#OPENED AN EMPTY FILE 
file = open('prac.txt', 'w')

#STORED EACH ITEM WITHIMN THE LIST INSIDE THE TEXT FILE
for movie in articles_new:
    # movie.remove(')')
    file.writelines(f"{movie}\n")
# for i in articles_new:
#     num = i[0]
#     nme = i[1]
#     file.write(f"{num} {nme}")



# name = heading.text
# new =name.split(')')

# print(heading)
# print(new)

# print(articles_new)



#I ALSO LEFT MY FAILURES HERE SO YOU COULD SEE THAT I'M HUMAN 
# PRACTICE MAKES PERFECT