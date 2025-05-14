from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = 'https://quotes.toscrape.com/js-delayed'

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get(url)
### Seleniumda find_element bulamazsa hata verir ama elements olduğu zaman boş liste verir.

##“Bir element hemen bulunamazsa, belirttiğim süre boyunca elementin ortaya çıkmasını dene.
## Süre bitince hâlâ yoksa hata ver.” buna az değer ver tüm elemenetleri aramasın zmn kaybı
driver.implicitly_wait(3)

##div.quote elementi sayfada görünür hale gelene kadar,en fazla 10 saniye boyunca bekle.
## Erken bulunursa hemen devam et.
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.quote'))
)

# Ne olursa olsun 10 saniye beklenir.
sleep(10)

contents = driver.find_elements(By.CSS_SELECTOR,'div.quote')
print(len(contents))