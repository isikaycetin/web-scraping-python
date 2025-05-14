import scrapy
from twisted.web.http import responses

# 1.adım pip install scrapy                        -> scrapy küt. indirdik
# 2.adım scrapy startproject books                 -> books adında klasör oluşturk
# 3.adım cd books                                  -> şimdi yapılan işlemler klasörün içinde
# 4.adım scrapy genspider book books.toscrape.com  -> book adında bir spider oluşturduk
# 5.adım scrapy view https://books.toscrape.com    -> kod direk sayfayı açar siteye göz atmak için kullanılır
#bazen hatalır veriler gelirse scrapy gözünden bakmak iyi olabilir.
# 6.adım scrapy shell https://books.toscrape.com   -> Scrapy'nin interaktif test ortamıdır.
# 7.adım scrapy crawl book -O books.json           -> kodu çalıştırmak için kullanılır eğer kaydetmek istiyorsak -O dosyadi.json yazmak lazım
# 8.adım cls                                       -> terminal temizlemek için

#### CSS SELECTOR ###

#--1. responce.css('')
#>>> prices = responce.css('p.price_color::text')
#selector olarak döndürür fiyatları döndürmez
#:: ? ne işe yarar  =>  ::text veya ::attr(...) ne işe yarar?
#::text → HTML etiketinin metin içeriğini alır.
#::attr(özellik) → HTML etiketinin bir attribute (özellik) değerini alır.

#--2. getall() hepsi get() ilk elemanı verir
#>>> prices = response.css('p.price_color::text').getall()
#bu ise fiyatların hepsini verir

#--3. alt sınıflara göre text çıkarmak
#first_name_css = response.css('article.product_pod h3 a::text').get()

#--4. attribute lere göre aramak
#1.yol => first_link_css = response.css('article.product_pod h3 a::attr(href)').get()
#2.yol =>  first_link_css = response.css('article.product_pod h3 a').attrib['href']

### XPATH SELECTOR  ####

#--1./text()
#first_name_xpath = response.xpath('//article[@class="product_pod"]/h3/a/text()').get()

#--2./@href
#1.yol => first_link_xpath = response.xpath('//article[@class="product_pod"]/h3/a/@href').get()
#2.yol => first_link_xpath = response.xpath('//article[@class="product_pod"]/h3/a').attrib['href']


class BooksItem(scrapy.Item):
    pass

#kendi oluşturduğumuz item sınıfı miras aldık içini
class BookItem(scrapy.Item):
    name = scrapy.Field()
    price_exc_tax = scrapy.Field()
    price_inc_tax = scrapy.Field()
    category = scrapy.Field()
    stars = scrapy.Field()
    upc = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    image_url = scrapy.Field()