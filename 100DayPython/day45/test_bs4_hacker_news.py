from bs4 import BeautifulSoup
import requests

response = requests.get(url = 'https://news.ycombinator.com/')
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
first_article_element = soup.select_one("td.title a")
first_article_element_content = first_article_element.string

score_first_article_element = soup.select_one('.subtext .score')
score_first_article_content = score_first_article_element.string.split(" ")[0]
print(score_first_article_content)