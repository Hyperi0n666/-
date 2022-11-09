import requests
from bs4 import BeautifulSoup as bs
from time import sleep
headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'}
for count in range(1,7):
    sleep(3)
    url = f"https://www.divan.ru/sankt-peterburg/category/myagkie-krovati/page-{count}"
    responce = requests.get(url, headers=headers )
    soup = bs(responce.text, "lxml")

    data = soup.find_all("div", class_='LlPhw')

    for i in data:
        price = i.find('span',class_='Zq2dF').text
        name = i.find('a',class_='ImmXq dpmhZ HyyHN ProductName').text
        print(price+'\n'+name+'\n\n')