from selenium import webdriver
from selenium.webdriver.common.by import By

url= 'https://books.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--headless') #tarayıcı arka plan çalışır biz görmeyiz

driver = webdriver.Chrome(options=options)
driver.get(url)

# Etiket ismi (tag name) ile element seçme
list_items = driver.find_elements(By.XPATH,'//li')
# list_item =driver.find_element(By.XPATH,'//li')
#print(len(list_items))

# Sınıf ismi (class name) ile element seçme
prices = driver.find_elements(By.XPATH,'//p[@class="price_color"]')
#for price in prices:
#    print(price.text)

# ID ile element seçme
body = driver.find_element(By.XPATH, '//body[@id="default"]')
#print(body.text)

# Özellikleri (attribute) kullanarak element seçme
alert = driver.find_element(By.XPATH, '//div[@role="alert"]')
#print(alert.text)

# İçindeki metni (text) kullanarak element seçme
next_button = driver.find_element(By.XPATH, '//a[text()="next"]')
#print(next_button.get_attribute('href'))

# İçiçe (nested) olan elementleri seçme
img_src = driver.find_element(By.XPATH, '//article[@class="product_pod"]/div/a/img').get_attribute('src')
#print(img_src)

# Navigasyon (siblings - parents)
# // belirtilen etiketi veya öğeyi DOM ağacının herhangi bir yerinde ara demektir
# / tek ögeyi bulur ilkini bulur.
# .. = Bir üst elemente (ebeveyn / parent) git demektir.
first_book = driver.find_element(By.XPATH, '//article[@class="product_pod"]')
first_book_div = first_book.find_element(By.XPATH, './div').get_attribute('class')
# print(first_book_div)
parent_of_first = first_book.find_element(By.XPATH, './..')
#print(parent_of_first.tag_name)

### Elementin siblingini bulma (kardeş)
# :: operatörü, ekseni (axis) belirtmek için kullanılır.
# ./ → "Şu anki elemandan itibaren ara" demek.
first_book = driver.find_element(By.XPATH, '//article[@class="product_pod"]')
parent_of_first = first_book.find_element(By.XPATH, './..')
# “İlk <li>'nin hemen sonraki kardeş <li> elementini getir” demektir.
# XPath'te [1], evet, "ilk eleman" demektir.
#Ama bu Python’daki gibi sıfırdan değil, 1’den başla
following_sibling = parent_of_first.find_element(By.XPATH, './following-sibling::li[1]')
second_book_name = following_sibling.find_element(By.XPATH, './article/div/a/img').get_attribute('alt')
print(second_book_name)