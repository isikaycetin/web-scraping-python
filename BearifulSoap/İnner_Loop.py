import requests
from bs4 import  BeautifulSoup


#Sayfalarda gezinerek her sayfada kaç kitap var onları yazdırmak 1.kısım bilinen sayfa sayısı 2.kısımda sayfa num bilinmiyorsa

url = 'https://books.toscrape.com/index.html'
response = requests.get(url)
#print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
#sayfa sayısı bulmak
page_counter = soup.find('li',class_='current').text
page_count_value = int(page_counter.split()[3])

#sayfa sayısı bilinoyorsa zaten biliyorduk 50 tane olduğunu
for page in range(1, page_count_value+1):
    print('------------------------------------')
    print(f'Şuan {page}.sayfada')


    page_url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    print(len(books), 'tane kitap var')

    for book in books:  # Bu satır, doğru girintiyle hizalanmalı
        book_url = 'https://books.toscrape.com/catalogue/' + book.find('a')['href']
        response = requests.get(book_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('div', class_='product_main').h1.text
        print(title)
        price = soup.find('div', class_='product_main').p.text
        print(price)
        print('------------------------------------')



