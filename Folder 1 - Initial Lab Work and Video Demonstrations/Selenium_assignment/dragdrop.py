from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

print("=" * 60)
print("Assignment - Drag and Drop Using Keyboard Actions")
print("=" * 60)
print("Page Title :", driver.title)
print("=" * 60)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

print("1. Source Element")
print("Text :", source.text)

print("2. Target Element")
print("Text :", target.text)

actions = ActionChains(driver)

actions.click_and_hold(source) \
       .move_to_element(target) \
       .release() \
       .perform()

time.sleep(2)

if "Dropped!" in target.text:
    print("Drag and Drop performed successfully.")
    print("Target Box Text :", target.text)
    
else:
    print("Drag and Drop failed.")

print("=" * 60)
print("Task completed successfully.")
print("=" * 60)

time.sleep(3)
driver.quit()