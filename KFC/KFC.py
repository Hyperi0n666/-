import requests
from bs4 import BeautifulSoup as bs
from time import sleep
headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'}

sleep(3)
url = f'https://www.kfc.ru/'
responce = requests.get(url,headers=headers)
soup = bs(responce.text, "lxml")

data = soup.find_all('a',class_='_1ptLJr9K6k condensed qRUtHPAJfM QQ_5t2PB0s')

data2 = soup.find_all('a',class_='_1ptLJr9K6k condensed qRUtHPAJfM')

for i in data:
    name = i.find('div',class_='_14ZQf5wtqx c-description').text
    price = i.find('span').text
    print(name +'\n' + price+'\n\n')
for j in data2:
    name = j.find('div',class_='_14ZQf5wtqx c-description').text
    price = j.find('span').text
    print(name +'\n' + price+'\n\n')    
