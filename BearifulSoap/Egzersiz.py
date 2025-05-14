import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
response.encoding = 'utf-8'


# 1.İlk quote'u yazdır (sözün kendisini metin olarak)
first_element = soup.find('div', class_='quote')
first_quote = first_element.span.text
# first_quote

# 2.İlk quote'un yazarının ismini yazdır
first_author = first_element.small.text
# first_author

# 3. İlk quote 'un etiketlerini yazdır (loop kullanmak gerekebilir)
tags = first_element.find_all('a', class_='tag')
#for tag in tags:
#    print(tag.text)

# 4. İlk sayfadaki tüm quote'ların bir listeini al. Eleman sayısını kontrol et, 10 olmalı.
first_element_all = soup.find_all('div', class_='quote')
#if first_element_all == 10:
#    print(first_element_all)

# 5. İlk sayfadaki tüm quote'ları, yazarlarını ve etiketlerini yazdır. (Loop kullanmak gerekiyor. Etiketler için bir loop daha.)
# for quote in soup.find_all('div', class_='quote'):
#     print(quote.span.text)
#     print(quote.small.text)
#     tags = quote.find_all('a', class_='tag')
#     for tag in tags:
#         print(tag.text)
#     print('\n')

# 6. Tüm sayfalardaki ilk yazarın ismini yazdır. (10 sayfa var. Yani 10 request yapmak ve 10 soup oluşturmak gerekiyor.)
# page = 1
# while True:
#     print(f'Page {page}')
#     page_url = f'https://quotes.toscrape.com/page/{page}/'
#     response = requests.get(page_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     next_page = soup.find('li', class_='next')
#     first_author = first_element.small.text
#     print(f'Yazarlar: {first_author}')
#     if next_page is None:
#         print("Son sayfaya ulaşıldı.")
#         break
#     else:
#         page += 1  # Burada page'i artırmalısınız

# 7. İlk sayfadaki 'Next' butonunu bul ve href değerini yazdır.
next = soup.find('li', class_='next')
next_href= next.a['href']
# print(next_href)

# 8. Bulduğun next butonunu kullanarak navigasyon ile (parent, sibling) ilk sayfadaki son quote elementine eriş.
last_quote = next.parent.parent.find_previous_sibling()
# print(last_quote)

# 9. Bulduğun son quote elementinin class ismini yazdır.
# print(last_quote['class'])

# 10.Bulduğun son quote elementinin 'itemtype' değerini yazdır.
print(last_quote['itemtype'])
