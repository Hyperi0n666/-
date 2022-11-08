import requests
from bs4 import BeautifulSoup as bs
from time import sleep
headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'}
for count in range(1,145):
    sleep(3)
    url = f"https://zenden.ru/catalog/women/?nav=page-{count}"
    responce = requests.get(url, headers=headers )
    soup = bs(responce.text, "lxml")

    data = soup.find_all("div", class_='products-list__item product-card product-card-new js-reveal')

    for i in data:
        image = i.find('img',class_='lazy').get("srcset").replace('2x','')
        name = i.find('div',class_='product-card__title js-productTitle').text
        price = i.find('span',class_='product-price__current').text
        print(image + '\n'+name+ '\n'+price+'\n\n')