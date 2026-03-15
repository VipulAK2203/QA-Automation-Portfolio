from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 3)

driver.get("https://www.flipkart.com")

search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@title = 'Search for Products, Brands and More']")))
search_box.click()
search_box.send_keys("iPhone")
search_box.send_keys(Keys.ENTER)
time.sleep(2)

first_product = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'ZFwe0M row']")))
product_title = first_product.find_element(By.XPATH, '//div[@class = "RG5Slk"]').text
print(product_title)
assert "iPhone" in product_title

product_price = first_product.find_element(By.XPATH, '//div[@class = "hZ3P6w DeU9vF"]').text
print(product_price)
assert product_price != ""

product_rating = first_product.find_element(By.XPATH, '//div[@class = "MKiFS6"]').text
print(product_rating)

first_product.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)




