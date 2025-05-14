import requests
from bs4 import BeautifulSoup
from pyexpat import features

url ='https://books.toscrape.com/'
response = requests.get(url) # Web sayfasından veriyi almak için HTTP GET isteği yapılır.
print(response.status_code) # HTTP isteği sonucu sayfa yüklenip yüklenmediğini kontrol eder.

#Sayfanın HTML içeriğini BeautifulSoup kullanarak analiz edilmesini sağlar.
# response.text: Web sayfasının HTML içeriği (metin formatında).
# 'html.parser': Python’un kendi HTML ayrıştırıcı
soup = BeautifulSoup(response.text , 'html.parser')
#print(soup.prettify()) # HTML içeriğini daha okunabilir ve düzenli bir şekilde ekrana yazdırır.