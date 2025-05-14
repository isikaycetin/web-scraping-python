import requests
from bs4 import  BeautifulSoup
from charset_normalizer.utils import unicode_range

#Sayfalarda gezinerek her sayfada kaç kitap var onları yazdırmak 1.kısım bilinen sayfa sayısı 2.kısımda sayfa num bilinmiyorsa

url = 'https://books.toscrape.com/index.html'
response = requests.get(url)
#print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
#sayfa sayısı bulmak
page_counter = soup.find('li',class_='current').text
page_count_value = int(page_counter.split()[3])

#sayfa sayısı bilinoyorsa zaten biliyorduk 50 tane olduğunu
# for page in range(1,page_count_value+1):
#     print(f'Şuan {page}.sayfada')
#     page_url = f'https://books.toscrape.com/catalogue/page-{page}.html'
#     response= requests.get(page_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     books = soup.find_all('article',class_='product_pod')
#     print(len(books),'tane kitap var')

unknown_page=1 # bunu mutlaka dışarı yaz yoksa döngü sıfırlanır hep 1.sayfa da kalır.
while True:
    print(f'Şuan {unknown_page}.sayfada')
    page_url = f'https://books.toscrape.com/catalogue/page-{unknown_page}.html'
    response= requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article',class_='product_pod')
    next = soup.find('li',class_='next')
    if next is None:
        break
    else:
       unknown_page+=1
