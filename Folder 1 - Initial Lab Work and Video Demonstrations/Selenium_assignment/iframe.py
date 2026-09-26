from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/nested_frames")
time.sleep(2)

print("\nTask 4 : Working with Frames")
print("-" * 60)

top_frame = driver.find_element(By.XPATH, "//frame[@name='frame-top']")
driver.switch_to.frame(top_frame)
print("Entered Top Frame")

middle_frame = driver.find_element(By.XPATH, "//frame[@name='frame-middle']")
driver.switch_to.frame(middle_frame)
print("Entered Middle Frame")

middle_text = driver.find_element(By.ID, "content").text
print("Content Available :", middle_text)

driver.switch_to.default_content()
print("Returned to Main Page")

print("Task Completed Successfully")
print("-" * 60)

time.sleep(3)
driver.quit()