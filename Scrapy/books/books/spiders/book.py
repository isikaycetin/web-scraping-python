import scrapy
from ..items import BookItem

number_dict ={'One':'1','Two':'2','Three':'3','Four':'4','Five':'5',}

# parantez içi miras alıyor
class BookSpider(scrapy.Spider):
    name = "book"
    # Bu bot yalnızca bu domain içinde gezinir.Örneğin, başka bir siteye yönlendirilirse kazıma işlemini engeller. (Güvenlik filtresi gibi düşünebilirsin.)
    allowed_domains = ["books.toscrape.com"]
    # Botun başlangıç yapacağı sayfa burası.Bu URL'den başlayıp parse() fonksiyonuna gider.
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books_links = response.css('article.product_pod h3 a::attr(href)').getall()
        for book_link in books_links:
           yield response.follow(book_link, callback=self.parse_books)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_books(self, response):
        book = BookItem()

        book['name'] = response.css('div.product_main h1::text').get()
        #xpath de [1] ilk eleman demek 0 yok xpath de
        book['price_exc_tax'] = response.xpath('//th[text()="Price (excl. tax)"]/following-sibling::td[1]/text()').get()
        book['price_inc_tax'] = response.xpath('//th[text()="Price (incl. tax)"]/following-sibling::td[1]/text()').get()
        book['upc'] = response.xpath('//th[text()="UPC"]/following-sibling::td[1]/text()').get()
        book['tax'] = response.xpath('//th[text()="Tax"]/following-sibling::td[1]/text()').get()
        book['availability'] = response.xpath('//th[text()="Availability"]/following-sibling::td[1]/text()').get()
        book['category'] = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
        book['image_url'] = 'https://books.toscrape.com' + response.css('div.active img').attrib['src'][5:]

        count_stars = response.css('p.star-rating')
        count_stars_class = count_stars.attrib['class']
        stars = count_stars_class.split()[-1]
        book['stars'] = number_dict[stars]

        yield book
        # bunu sadece bir kitap için yaptığı için çünkü for içinde değil bu bir fonksiyon o yüzden hepsi içim yapması için yield kullandık
