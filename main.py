from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Location to our Chrome driver:
service = Service('C:\\Users\\hartm\\iCloudDrive\\chrome_driver\\chromedriver.exe')

# xpath to element we want to scrape:
xpath1 = "/html/body/div[1]/div/h1[1]"
xpath2 = "/html/body/div[1]/div/h1[2]"


# Create driver and set options:
def get_driver():
    # Options for better and easier scraping ###
    # Create ChromeOptions instance:
    options = webdriver.ChromeOptions()
    # Flag to disable infobars:
    options.add_argument("disable-infobars")
    # Flag to start browser as maximized
    options.add_argument("start-maximized")
    # For those running linux:
    options.add_argument("disable-dev-shm-usage")
    # Disable browser sandbox:
    options.add_argument("no-sandbox")
    # Help get around anti-scraping features:
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    # Chrome class of webdriver with path to our chrome driver
    driver = webdriver.Chrome(service=service, options=options)
    # Connect to webpage:
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """Extract the temp from text"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by=By.XPATH, value=xpath2)
    # return element.text
    return clean_text(element.text)

print(main())
