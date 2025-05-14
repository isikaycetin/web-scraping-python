from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import openpyxl


def login(the_driver):
    login_button = the_driver.find_element(By.XPATH, '//a[text()="Login"]')
    login_button.click()

    username_input = the_driver.find_element(By.XPATH, '//input[@id="username"]')
    username_input.send_keys('Işıkay')

    password_input = the_driver.find_element(By.XPATH, '//input[@id="password"]')
    password_input.send_keys('123456')

    input = the_driver.find_element(By.XPATH, '//input[@value="Login"]')
    input.click()

url= 'https://quotes.toscrape.com/'
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

dict = {'quote':[],'author':[],'tags':[]}
def scrape_page(the_driver):

    contents = the_driver.find_elements(By.CSS_SELECTOR,'div.quote')
    print(len(contents))
    for content in contents:
        text_ = content.find_element(By.CLASS_NAME, 'text').text
        author = content.find_element(By.CLASS_NAME, 'author').text
        tag_elements = content.find_elements(By.CLASS_NAME, 'tags')  # her bir quote içindeki tag'ler

        dict['quote'].append(text_)
        dict['author'].append(author)
        dict['tags'].append(tag_elements)

        # print(text_)
        # print(author)
        # print("Etiketler:")
        # for tag in tag_elements:
        #     print("-", tag.text)
        # print("-" * 30)

        # tag_elements = content.find_elements(By.CSS_SELECTOR, '.tags a.tag')  # sadece etiket linklerini alıyoruz
        #
        # tags = [tag.text for tag in tag_elements]
        #
        # print("Alıntı:", text_)
        # print("Yazar:", author)
        # join listeleri birleştirmek için kullanılır
        # print("Etiketler:", ", ".join(tags))

driver = webdriver.Chrome(options=options)
driver.get(url)

login(driver)

while True:
    scrape_page(driver)
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.next a'))
        )
        next_button.click()
    except Exception as e:
        print("Hata aldınız sayfalara geçemiyoruz:", e)
        break

# Kodu bitirince tarayıcıyı kapatma

#driver.quit()

# df = pd.DataFrame(dict)
# df.to_excel('quotes.xlsx')