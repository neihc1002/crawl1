import requests
from bs4 import BeautifulSoup
import json


def get(page):
    response = requests.get("https://agirlmagazine.tumblr.com/page/{0}".format(page))
    soup = BeautifulSoup(response.content, "html.parser")
    all = soup.find("div", {"id": "grid"})
    links = [link.get("data-photo-high") for link in all.findAll("div", {"class": "gridphoto"})]
    return links

if __name__ == "__main__":
    data = {}
    data['girl'] = []
    id = 1
    for x in range(1):
        link = get(x+1)
        for l in link:
            data['girl'].append({"id": id, 'url': l})
            id+1;
    with open('./data/data.json', 'w') as outfile:
        json.dump(data, outfile)