from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

print("Page Title :", driver.title)
print("=" * 60)

mouse_hover = driver.find_element(By.CLASS_NAME, "dropbtn")

actions = ActionChains(driver)
actions.move_to_element(mouse_hover).perform()

print("Mouse hovered over 'Mouse Hover' menu successfully.")

time.sleep(2)

mobiles = driver.find_element(By.LINK_TEXT, "Mobiles")
print("Menu Item :", mobiles.text)

mobiles.click()

print("Mobiles option selected successfully.")

print("Task completed successfully.")
print("=" * 60)

time.sleep(3)
driver.quit()