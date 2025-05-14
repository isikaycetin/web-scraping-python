import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
response.encoding = 'utf-8'

#başlık yazdırmak için A Light in the Attic
title = soup.find('div', class_='product_main').h1.text
# print(title)

price = soup.find('div', class_='product_main').p.text
#print(price)

ul = soup.find('ul', class_='breadcrumb')
li = ul.find_all('li')[2]
category = li.find('a').text
#print(category)

#yıldız sayısını bulmak içn
# burada kaç rating olduğunu bulmak için class ına ulaşmalıyız.
dict = {'One':1, 'Two':2, 'Three':3, 'Four':4,'Five':5}
rating = soup.find('p',class_='star-rating')
rating_class = rating['class'] # class=star-rating Three  burada three ye ulaşmalıyız.
rating_class_number= rating_class[1] # sayı değerine ulaşmak için => star-rating Three
finded_rating = dict[rating_class_number] #bulunan değeri sözlükte yerine koy.
#print(finded_rating)

#upc bulma
upc = soup.find('th', string='UPC')
upc_sibling = upc.find_next_sibling().text
#print(upc_sibling)

# stok adedim yazısyıla birlikte => In stock (22 available)
Availability = soup.find('th', string='Availability')
availability = Availability.find_next_sibling().text
#print(availability)

#şimdi de sadece sayısal kısmı istiyoruz yani sadece ekranda 22 availabeş
#SPLİT: Bir string'i ayraçlara göre parçalara ayırır, bir liste döndürür
#STRİP:Ne işe yarar?: Bir string'in başındaki ve sonundaki belirtilen karakterleri (varsayılan olarak boşlukları) temizler.

#In stock (22 available) => (22 available)
# Burada, "In stock " ifadesine göre metni böldün.
# Bu işlem sonucu, "In stock " ifadesinden sonrasındaki kısmı aldık.
# Eğer availability = "In stock (22 available)" ise, bu işlem bize "(22 available)" kısmını verecek.
in_stock = availability.split("In stock ")[1]  #['', '(22 available)'] => (22 available)
in_in_stock = in_stock.split("available")[0]
in_in_stock = in_in_stock.strip("() ")  # Parantezleri ve boşlukları temizledik
#print(in_in_stock)

#Resim linkini bulmak
img_link = 'https://books.toscrape.com/'+soup.find('div', class_='item').img['src'][6:]
#print(img_link)