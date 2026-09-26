from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

print("=" * 60)
print(" Alert Popup")
print("=" * 60)
print("Page Title :", driver.title)
print("=" * 60)
print("1. Generating Simple Alert Popup")

simple_alert_button = driver.find_element(
    By.ID,
    "alertBtn"
)

simple_alert_button.click()
print("Simple Alert Popup generated successfully.")

time.sleep(2)

alert = Alert(driver)

print("Alert Message :", alert.text)

alert.accept()
print("Alert accepted successfully.")


time.sleep(2)

driver.quit()