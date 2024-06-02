from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up the Chrome WebDriver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    driver.get("https://resumecraft01.netlify.app/")
    
    # Click on the LOGIN link
    login_link = driver.find_element(By.LINK_TEXT, "LOGIN")
    login_link.click()

    # Wait for the login page to load
    time.sleep(2)

    # Find the email input field by its placeholder and clear any existing data, then input the email
    email_field = driver.find_element(By.CSS_SELECTOR, "[placeholder='Email']")
    email_field.clear()
    email_field.send_keys("vajovi7334@acuxi.com")

    # Find the password input field by its placeholder and clear any existing data, then input the password
    password_field = driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']")
    password_field.clear()
    password_field.send_keys("kk1234")

    # Find the LOGIN button by its CSS class and click it
    login_button = driver.find_element(By.CSS_SELECTOR, ".bg-c-primary.text-white")
    login_button.click()

    # Wait for some time to ensure the login process is completed properly
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)
    # If any error occurs, print it and keep the browser open for debugging purposes

# No need to quit the browser here as per your requirement
