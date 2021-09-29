import bs4
import requests
import re

def get_links(url):
    href_regex = re.compile(r"(.*://)?(.*)")

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    tags = soup.find_all("a", href=True)
    result = []
    for tag in tags:
        if href_regex.match(tag["href"]) != None:
            result.append(href_regex.match(tag["href"])[2])
    return result