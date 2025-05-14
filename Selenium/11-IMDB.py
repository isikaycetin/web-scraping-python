from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = 'https://www.imdb.com/search/title/?title_type=feature&genres=action&groups=oscar_winner'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(1)
driver.get(url)
sleep(2)

def cookies():
    try:
        cookie_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.icb-btn'))
        )
        cookie_btn.click()
        print("Çerezler kabul edildi.")
    except Exception as e:
        print("Çerez butonuna tıklanamadı:", e)

cookies()
sleep(1)
director_links = []

# Tüm içerikleri yükle
while True:
    try:
        more_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.ipc-see-more__text'))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", more_button)
        sleep(1)
        more_button.click()
    except:
        print("Tüm içerikler yüklendi.")
        break

# Info butonlarını al
svg_i_buttons = driver.find_elements(By.CSS_SELECTOR, 'div.dli-post-element')
print(f"{len(svg_i_buttons)} adet info butonu bulundu.")

# Her info butonuna tıkla, linki al, pencereyi kapat
for svg_i_button in svg_i_buttons:
    try:
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", svg_i_button)
        sleep(0.3)
        driver.execute_script("arguments[0].click();", svg_i_button)
        sleep(0.5)

        a_tag = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.bDaEhW'))
        )
        link = a_tag.get_attribute('href')
        print(link)
        director_links.append(link)

        close_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ipc-promptable-base__close'))
        )
        driver.execute_script("arguments[0].click();", close_btn)
        sleep(0.3)

    except Exception as e:
        print("Hata oldu ama devam ediliyor:", e)
        continue






# driver.execute_script('arguments[0].click()', results_button)


# def guvenli_tikla(driver, actions, element):
#     try:
#         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))
#         actions.move_to_element(element).click().perform()
#         return True
#     except Exception as e:
#         print("Tıklama hatası:", e)
#         return False

