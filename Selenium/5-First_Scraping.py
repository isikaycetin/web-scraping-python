from selenium import webdriver
from selenium.webdriver.common.by import By

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

def scrape_page(the_driver):

    contents = the_driver.find_elements(By.CSS_SELECTOR,'div.quote')

    for content in contents:
        text_ = content.find_element(By.CLASS_NAME, 'text').text
        author = content.find_element(By.CLASS_NAME, 'author').text
        tag_elements = content.find_elements(By.CLASS_NAME, 'tags')  # her bir quote içindeki tag'ler

        print(text_)
        print(author)
        print("Etiketler:")
        for tag in tag_elements:
            print("-", tag.text)
        print("-" * 30)

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
scrape_page(driver)
