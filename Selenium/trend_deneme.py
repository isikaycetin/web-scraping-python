from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL
url = "https://www.trendyol.com/sr?wb=107655%2C105536&wc=103108&lc=103108&qt=laptop&st=laptop&tag=turuncu_kampanya_urunu&os=1"

# Tarayıcı ayarları
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(3)

scroll_pause_time = 1
scroll_step = 500  # her seferinde 500px aşağı kaydır
max_scroll = 30  # kaç kez kaydırılacak
last_height = 0

for i in range(max_scroll):
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    time.sleep(scroll_pause_time)

    current_height = driver.execute_script("return window.pageYOffset + window.innerHeight;")
    total_height = driver.execute_script("return document.body.scrollHeight;")

    print(f"Scroll {i + 1}: {current_height}/{total_height}")

    if current_height >= total_height:
        print("Sayfa sonuna ulaşıldı.")
        break

print("Scroll işlemi tamamlandı.\nÜrünler çekiliyor...")

# Ürün kartlarını al
urun_kartlari = driver.find_elements(By.CLASS_NAME, "p-card-wrppr")
print(f"{len(urun_kartlari)} ürün bulundu.\n")

for urun in urun_kartlari:
    try:
        isim = urun.find_element(By.CLASS_NAME, "prdct-desc-cntnr-name").text
    except:
        isim = "Ürün adı yok"

    try:
        fiyat = urun.find_element(By.CLASS_NAME, "prdct-desc-cntnr-ttl-w").text
    except:
        fiyat = "Fiyat yok"

    try:
        link = urun.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        link = "Link yok"

    print(f"Ad: {isim}\nFiyat: {fiyat}\nLink: {link}\n")


#         # Yeni sekmede detaylara bakmak için ayrı bir pencere açma yöntemi önerilir.
#         driver.execute_script("window.open('');")
#         driver.switch_to.window(driver.window_handles[1])
#         driver.get(link)
#         time.sleep(2)
#
#         try:
#             detay = driver.find_element(By.CLASS_NAME, "detail-name-container").text
#         except:
#             detay = "Detay yok"
#
#         # Sekmeyi kapat ve eski sekmeye dön
#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])
#
#         nesneler.append({
#             "isim": isim,
#             "fiyat": fiyat,
#             "link": link,
#             "detay": detay
#         })
#
#         print(f"Kitap: {isim}\nFiyat: {fiyat}\nLink: {link}\nDetay: {detay}\n")
#
#     # Sayfada "Next" butonu var mı?
#     try:
#         next_button = driver.find_element(By.CLASS_NAME, "pagination__next")
#         if "disabled" in next_button.get_attribute("class"):
#             print("Sonraki sayfa yok. Sonlanıyor...")
#             break
#         else:
#             next_button.click()
#             time.sleep(3)
#     except:
#         print("Next butonu bulunamadı. Sonlanıyor...")
#         break
#
# # Verileri yazdır
# print("\nTüm Kitaplar ve Detaylar:")
# for nesne in nesneler:
#     print(f"{arama} : {nesne['isim']}, Fiyat: {nesne['fiyat']}, Link: {nesne['link']}, Detay: {nesne['detay']}")
