from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://quotes.toscrape.com/js'

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get(url)

### Diyelimki bu kodda sıkıntı var tıklamadı. O zaman actionları kullanmalısıns
# next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a'))
# next_button.click()

### 1-move_to_element(elem) 2-click(elem) 3-send_keys("...") 4-perform():uygulamak için bu olamadan olmaz.
next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a')
actions = ActionChains(driver)
actions.move_to_element(next_button).perform()