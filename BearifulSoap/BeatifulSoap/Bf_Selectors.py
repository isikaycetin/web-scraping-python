import requests
from bs4 import BeautifulSoup

url ='https://quotes.toscrape.com/'
response = requests.get(url)
#print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title')  #find(element,class)
#title = soup.title
#HTML ya da XML belgelerindeki belirli bir öğeyi (tag) aramak için kullanılır
#print(title)