import requests
from bs4 import BeautifulSoup
import json
import sqlite3 as lite
import os

def get(page):
    response = requests.get("https://agirlmagazine.tumblr.com/page/{0}".format(page))
    soup = BeautifulSoup(response.content, "html.parser")
    all = soup.find("div", {"id": "grid"})
    links = [link.get("data-photo-high") for link in all.findAll("div", {"class": "gridphoto"})]
    return links

if __name__ == "__main__":
    con = None
    path = os.path.dirname(__file__) + "\\test.db"
    con = lite.connect(path)
    page = os.getenv("PAGE", "1")
    data = {}
    data['girl'] = []
    id = 1
    links = []
    for x in range(int(page)):
        link = get(x+1)
        links.extend(link)
    for l in links:
        data['girl'].append({"id": id, 'url': l})
        id+=1;

    with open('./data/data.json', 'w') as outfile:
        json.dump(data, outfile)