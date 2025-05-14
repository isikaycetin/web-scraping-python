from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import openpyxl


url = 'https://quotes.toscrape.com/'

options = webdriver.ChromeOptions()
# options.add_argument('start-maximized')
# options.add_experimental_option('detach', True)
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get(url)

dict = {
    'name':[],
    'birth_date':[],
    'birth_place':[]
}

link =[]

## 1.Soru:Giriş yap
def login():
    login_a = driver.find_element(By.XPATH,'//a[text()="Login"]')
    login_a.click()

    username = driver.find_element(By.ID,'username')
    username.send_keys("Işıkay")

    password = driver.find_element(By.ID,'password')
    password.send_keys("isikay17")

    input = driver.find_element(By.XPATH,'//input[@value="Login"]')
    input.click()

try:
    login()
except Exception as e:
    print("giriş yapılamadı bir hata var!!")


## 2.Soru: Tüm sayfaları gez
#all_quotes = []
while True:
    quotes = driver.find_elements(By.XPATH,'//div[@class="quote"]')
#    all_quotes.extend(quotes)  # extend direk ekle [ [1,2,3 ] ] böyle olmasını engeller -> [1,2,3]

    for quote in quotes:
        author_link = quote.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        link.append(author_link)
    try:
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.next a'))
        )
        next_button.click()
    except:
        break

# Aynı olan linkleri elemek için set() de kullanabilirdik ama daha temel olsun istedim
# unique_link = list(set(link))
unique_link= []
for item in link:
    if item not in unique_link:
        unique_link.append(item)
# print(unique_link)

# isim, doğum tarihi ve doğum yerini elde edip bunları dictionary'e ekleyin.
def author_info():
     for unique_link_in in unique_link:
         driver.get(unique_link_in)
         name = driver.find_element(By.CSS_SELECTOR, 'h3.author-title').text
         dict['name'].append(name)

         birth_date = driver.find_element(By.CSS_SELECTOR, 'span.author-born-date').text
         dict['birth_date'].append(birth_date)

         birth_place = driver.find_element(By.CSS_SELECTOR, 'span.author-born-location').text
         dict['birth_place'].append(birth_place)

author_info()
df = pd.DataFrame(dict)
df.to_excel('yazarlar.xlsx')
