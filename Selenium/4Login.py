from selenium import webdriver
from selenium.webdriver.common.by import By

url= 'https://quotes.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

def login(the_driver):

    login_button = the_driver.find_element(By.XPATH, '//a[text()="Login"]')
    login_button.click()

    username_input = the_driver.find_element(By.XPATH, '//input[@id="username"]')
    username_input.send_keys('Işıkay')

    password_input = the_driver.find_element(By.XPATH, '//input[@id="password"]')
    password_input.send_keys('123456')

    input = the_driver.find_element(By.XPATH, '//input[@value="Login"]')
    input.click()

driver = webdriver.Chrome(options=options)
driver.get(url)

login(driver)
