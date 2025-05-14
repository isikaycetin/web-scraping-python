from selenium import webdriver
from selenium.webdriver.common.by import By

url= 'https://books.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--headless') #tarayıcı arka plan çalışır biz görmeyiz

driver = webdriver.Chrome(options=options)
driver.get(url)

#Etiket İsmi ile tag seçme
list_items = driver.find_elements(By.CSS_SELECTOR ,"li") #75 tane li varmış.
list_item = driver.find_element(By.CSS_SELECTOR, 'li').text
# print(list_item)

# Sınıf ismi (class name) ile element seçme
#1.Tüm p elementleri
prices = driver.find_elements(By.CSS_SELECTOR, 'p.price_color')
#for price in prices:
#     print(price.text)

#ID ye göre element seçmek
body = driver.find_element(By.CSS_SELECTOR, 'body#default')
body_ = driver.find_element(By.ID, 'default')
#print(body_.text)

#Attribute lere göre element seçmek
alert = driver.find_element(By.CSS_SELECTOR,'div[role="alert"]')
#print(alert.text)

# İçindeki metni (text) kullanarak element seçme
# bu özellik css de yok XPATH de var

# İçiçe (nested) olan elementleri seçme  .get_attribute()
img_src = driver.find_element(By.CSS_SELECTOR,'article.product_pod div a img').get_attribute('src')
#print(img_src)

