import datetime
import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def pagination(path):
    global result
    url = f'https://www.vatanbilgisayar.com/{path}/?page=300'
    response = requests.get(url)

    with open(f'index.html', 'w') as f:
        f.write(response.text)

    with open('index.html') as f:
        scr = f.read()

    soup = BeautifulSoup(scr, 'lxml')

    for i in soup.find_all('a', class_='pagination__content'):
        result = i.text
    return result


def collect_data():
    path = 'apple/notebook'
    pagination_count = pagination(path)

    for i in range(1, int(pagination_count) + 1):
        url = f'https://www.vatanbilgisayar.com/{path}/?page={i}'
        print(url)
    # cards = soup.find_all('div', class_='product-list product-list--list-page')
    #
    #
    # # json_data = {
    # #     "total":
    # # }
    #
    # # with open('json_data', 'w') as f:
    # #     json.dump(json_data, f)
    #
    # for cards in cards:
    #     cards_name = cards.find('div', class_='product-list__product-name').text.strip()


def main():
    collect_data()


if __name__ == '__main__':
    main()
