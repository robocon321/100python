import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url = url)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
movies = soup.select("h3.title")

with open('movies.txt', 'a', encoding="utf-8") as file:
    for i in range(len(movies) - 1, -1, -1):
        file.write(movies[i].getText()+"\n")
