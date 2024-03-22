from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Setup Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH

# Navigate to the game URL
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie element by its ID
cookie = driver.find_element(by=By.ID, value="cookie")

# Define the end time (1 minute from now) and the timeout (5 seconds from now)
timeout = time.time() + 5
end_time = time.time() + 1 * 60

# Last time we checked for upgrades
last_check = time.time()


# Function to get the number of cookies
def get_cookies():
    return int(driver.find_element(By.ID, "money").text.replace(",", ""))


# Main loop
try:
    while time.time() < end_time:
        cookie.click()

        # when the amount of cookies is greater than the price of the item buy it
        if get_cookies() >= 300:
            driver.find_element(By.ID, "buyGrandma").click()

finally:
    # Print cookies/second
    cps = driver.find_element(By.ID, "cps").text
    print(f"Cookies/second: {cps}")

    # Cleanup and close the browser window
    driver.quit()
