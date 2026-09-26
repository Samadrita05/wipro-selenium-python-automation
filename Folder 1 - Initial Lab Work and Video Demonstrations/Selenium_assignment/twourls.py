from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
print("First URL opened.")

driver.maximize_window() 

driver.switch_to.new_window("tab")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print("Second URL opened.")

print("=" * 60)
print("Opening two URL's successfully.")

print("Task completed successfully.")
print("=" * 60)

time.sleep(3)

driver.quit()