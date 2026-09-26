from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)

parent_window = driver.current_window_handle
print("Parent Window:", parent_window)

driver.find_element(By.ID, "opentab").click()
time.sleep(3)

windows = driver.window_handles

for window in windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

print("Current URL:", driver.current_url)

time.sleep(3)

driver.close()

driver.switch_to.window(parent_window)

print("Returned to Parent Tab")

name_box = driver.find_element(By.ID, "name")
name_box.send_keys("Samadrita Hazra")

print("\nName entered successfully.")
print("=" * 60)

time.sleep(5)

driver.quit()