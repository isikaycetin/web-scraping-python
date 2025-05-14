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

while True:
    try:
        # Şu ana kadar listelenen info butonlarını al
        info_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.ipc-icon-button')
        print(f"Şu ana kadar {len(info_buttons)} buton var.")

        for i in range(len(director_links), len(info_buttons)):
            try:
                info_button = info_buttons[i]
                actions.move_to_element(info_button).perform()
                sleep(0.3)
                info_button.click()
                sleep(0.5)

                # Linki al
                a_tag = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.bDaEhW'))
                )
                link = a_tag.get_attribute('href')
                print(link)
                director_links.append(link)

                # Kapat
                close_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ipc-promptable-base__close'))
                )
                close_btn.click()
                sleep(0.5)

            except Exception as e:
                print("Kazıma sırasında hata oldu, devam ediliyor:", e)
                continue

        # Load More butonuna tıkla (varsa)
        more_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.ipc-see-more__text'))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", more_button)
        sleep(1)
        more_button.click()
        sleep(1)

    except Exception as e:
        print("Tüm butonlar yüklendi ya da tıklanamadı, döngü kırılıyor:", e)
        break

print(f"Toplam {len(director_links)} link kazındı.")
