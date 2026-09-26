from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

print("\nTask 5 : Working with different id")
print("-" * 60)

product_table = driver.find_element(By.ID, "productTable")
driver.execute_script("arguments[0].scrollIntoView();", product_table)
time.sleep(2)

required_rows = [1, 3, 5]

all_rows = driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr")

for index, row in enumerate(all_rows, start=1):
    if index in required_rows:
        row.find_element(By.XPATH, "./td[4]/input").click()
        item = row.find_element(By.XPATH, "./td[2]").text
        print("Selected Product:", item)

print("\nTask completed successfully")
print("=" * 60)

time.sleep(3)
driver.quit()