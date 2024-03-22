from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.nl/JANSNO-mechanische-schijfremmen-elektrische-volwassenen/dp/B0C65S3ZQL/ref=lp_16545839031_1_1?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is: ${price_dollar.text}.{price_cents.text}")

driver.quit()
