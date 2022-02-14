from bs4 import BeautifulSoup
import requests
import json

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

url = "https://socratify.net/quotes/best"
content_page = requests.get(url, headers=HEADER)


def get_content(page):
    soup = BeautifulSoup(page.text, "html.parser")
    content = soup.findAll("div", class_="b-list-quote2__item")
    # quotes = content.findAll("div", class_="b-list-quote2__item ")
    obj = []

    for x in content:
        title = x.find("a", class_='b-list-quote2__item-text js-quote-text').text
        author = x.find("div", class_="b-list-quote2__item-category").a.text
        item = {
            "title": title.strip(),
            "author": author.strip()
        }
        obj.append(item)
    return obj


# get_content(content_page)


def write_json():
    with open("quotes.json", "w") as write_file:
        json.dump(obj, write_file)


def read_json():
    with open("quotes.json", "r") as read_file:
        print(dir(read_file))


# write_json()
read_json()
