from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

print("=" * 60)
print(" Uploading  a File through automation")
print("=" * 60)

file_path = r"D:\.vscode\Selenium_assignment\sample.txt"

file_upload = driver.find_element(By.ID, "singleFileInput")
file_upload.send_keys(file_path)


print("Selected File :", file_path)

driver.find_element(By.XPATH, "//button[text()='Upload Single File']").click()
time.sleep(2)

status = driver.find_element(By.ID, "singleFileStatus").text
print("Upload Status :", status)

print("File uploading completed successfully.")
print("=" * 60)

time.sleep(5)
driver.quit()