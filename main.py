import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
y_c_webpage = response.text

soup = BeautifulSoup(y_c_webpage,"html.parser")

num = 1
title_h3 = soup.find_all(class_="listicleItem_listicle-item__title__BfenH")

for i in title_h3:
    title_split = i.text.split()
    del title_split[0]
    movie = ' '.join(title_split)

    with open("movies.txt",mode='a') as file:
        file.write(f"{num}) {movie}\n")
    num +=1




















# head_names = soup.find_all(name="a")
# # <span class="score" id="score_40003710">346 points</span>
#
# no_points = soup.find(class_="titleline")
# anchor_tag = no_points.select_one(selector="a")
# print(anchor_tag["href"])
# print(no_points.text)
# points = soup.find(name="span",class_="score")
# print(points.text)


































# with open("website.html") as file:
#     print(file.read())
