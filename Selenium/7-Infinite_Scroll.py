from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://quotes.toscrape.com/scroll'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get(url)

# window.scrollTo(x, y): Sayfayı x ve y koordinatlarına kaydırır.
# 0: Yatay kaydırma yok.
# document.body.scrollHeight: Sayfanın dikeydeki tüm yüksekliğidir (sayfanın en altı).
sleep(2)
old_height= driver.execute_script("return document.body.scrollHeight")

def scrolling():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # sleep(1)
    # taramalı gibi beklemez hemen kaydırır.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'div.quote'))
    )

while True:
    scrolling()
    new_height= driver.execute_script("return document.body.scrollHeight")
    if new_height == old_height:
        break
    old_height = new_height

contents = driver.find_elements(By.CSS_SELECTOR,'div.quote')
print(len(contents))

# element = driver.find_element(...)
# driver.execute_script("arguments[0].scrollIntoView(true);", element)
# JavaScript fonksiyonudur ve bir elementi görünür alana (viewport) kaydırır.
# "arguments[0]" = Python'dan JavaScript'e gönderdiğin element

# scrollBy(x, y)
# Sayfayı bulunduğun konuma göre kaydırır.
# Yani "şu kadar daha git" demek gib

# scrollTo(x, y)
# Sayfayı belirli bir koordinata kaydırır.
# Yani "direkt şu noktaya git" demek gibi.