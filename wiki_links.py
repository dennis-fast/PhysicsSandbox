from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def get_internal_links(_start_link):
    html = urlopen(_start_link)
    soup = BeautifulSoup(html, "html.parser")

    internal_links = []

    # regex string returns all links that start with /wiki/ and after that do not contain any colons
    for _link in soup.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in _link.attrs:
            internal_links.append(str("https://en.wikipedia.org" + _link.attrs['href']))

    return list(set(internal_links))


initial_link = "https://en.wikipedia.org/wiki/Felix_Gers"
first_level_links = get_internal_links(initial_link)

second_level_links = []
for _l in first_level_links:
    second_level_links.append(get_internal_links(_l))

print("Information retrieved for:", initial_link)
print("First level links:", len(first_level_links))
print("Second level links:", sum(len(row) for row in second_level_links))