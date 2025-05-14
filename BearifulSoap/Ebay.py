import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import time

url = 'https://www.ebay.com/sch/i.html?_nkw=laptop&_sacat=0&_from=R40&_oaa=1&RAM%2520Size=64%2520GB&rt=nc&Screen%2520Size=12%252D12%252E9%2520in%7C14%252D14%252E9%2520in&_dcat=177'

dict = {
    'name':[],
    'price':[],
    'shipping':[],
     'link':[]
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

response= requests.get(url, headers=headers)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

page_number = 1
while True:
     print(f'Page {page_number}')
     laptop_url = f'https://www.ebay.com/sch/i.html?_nkw=laptop&_sacat=0&_from=R40&_oaa=1&RAM%2520Size=64%2520GB&rt=nc&Screen%2520Size=12%252D12%252E9%2520in%7C14%252D14%252E9%2520in&_dcat=177&_pgn={page_number}'
     response_ = requests.get(laptop_url, headers=headers)
     soup = BeautifulSoup(response_.text, "html.parser")
     laptops = soup.find_all('div', class_='s-item__wrapper')
     prices = soup.find_all('span', class_='s-item__price')
     for laptop in laptops:
      name = laptop.find('div', attrs={'class':'s-item__title'}).text
      print(name)
      print('------------------------')
     next_button = soup.find('a', class_='pagination__next')
     if not next_button:  # Eğer 'Next' butonu yoksa (son sayfadaysanız)
         print("No more pages, stopping the loop.")
         break
     page_number += 1



