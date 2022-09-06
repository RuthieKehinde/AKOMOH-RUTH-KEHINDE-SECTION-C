import numpy as np
a = 2
print(a)
from bs4 import BeautifulSoup
import requests
from csv import writer


url ="https://www.pararius.com/apartments/delft"
web = requests.get(url)
print(web)
soup = BeautifulSoup(web.content, 'html.parser')
lists= soup.find_all('section', class_="listing-search-item listing-search-item--list listing-search-item--for-rent")

with open('housing.csv', 'w', encoding='utf8',newline='') as f:
    thewriter  = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="listing-search-item__link listing-search-item__link--title").text.replace('\n', '')
        location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')
        area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text.replace(
        '\n', '')

        info = [title, location, price, area]
        thewriter.writerow(info)




