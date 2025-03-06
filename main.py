import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, 'html.parser')

h2_tags = soup.find_all('h2')

movie_titles = []
for h2 in h2_tags:
    movie_title = h2.find('strong')
    if movie_title:
        movie_titles.append(movie_title.getText())

for movie in movie_titles[::-1]:
    with open('movies.txt', 'a') as file:
        file.write(f"{movie}\n")


