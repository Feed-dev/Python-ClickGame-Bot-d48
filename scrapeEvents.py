from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.headless = True  # Run in headless mode to avoid opening a browser window
driver = webdriver.Chrome(options=options)

# Open the page
driver.get("https://www.python.org/events/")

# Pause to ensure page loads completely
time.sleep(5)  # Adjust this delay as necessary

# Locate elements containing event dates and titles
events = driver.find_elements(By.XPATH, "//ul[contains(@class, 'list-recent-events')]/li")

# Initialize a dictionary to store event data
event_data = {}

# Extract and store event data
for i, event in enumerate(events, start=1):
    try:
        title = event.find_element(By.XPATH, "./h3/a").text
        date = event.find_element(By.XPATH, "./p/time").text
        event_data[f"event_{i}"] = {"time": date, "name": title}
    except Exception as e:
        print(f"Error processing event {i}: {e}")

# Print the dictionary
print(event_data)

# Cleanup
driver.quit()
