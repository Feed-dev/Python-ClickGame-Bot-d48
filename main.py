from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Selenium WebDriver without headless mode to see the browser
driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and added to your PATH

# Navigate to the game URL
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Define the end time (5 minutes from now)
end_time = time.time() + 5 * 60

# Find the cookie element by its ID using the updated method
cookie = driver.find_element(By.ID, 'cookie')

# Click on the cookie as fast as possible in a loop
try:
    while True:
        cookie.click()
        # Optional: Adjust the sleep time to control the click speed
        # time.sleep(0.01)
except KeyboardInterrupt:
    print("Stopping the cookie clicker bot.")

# Comment or uncomment based on your preference
# driver.quit()
