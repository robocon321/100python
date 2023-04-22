from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# all_anchor_tags = soup.find_all(name = "a")
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name = "h1", id = "name")
name = soup.select("li")
print(name)