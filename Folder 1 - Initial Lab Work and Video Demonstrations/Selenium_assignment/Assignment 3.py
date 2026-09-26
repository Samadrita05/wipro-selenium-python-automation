from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

print("=" * 60)
print("Assignment 3 - CSS Selector Challenge")
print("=" * 60)
print("Page Title :", driver.title)
print("=" * 60)
print("\n1. CSS Selector using ID\n")

name_field = driver.find_element(By.CSS_SELECTOR, "#name")
name_field.send_keys("User")

print("Successfully located Name field using CSS ID Selector (#name)")

time.sleep(2)

print("\n2. CSS Selector using Class\n")
email_field = driver.find_element(By.CSS_SELECTOR, ".form-control")
email_field.clear()
email_field.send_keys("sample@test.com")

print("Successfully located an element using CSS Class Selector (.form-control)")

time.sleep(2)

print("\n3. CSS Selector using Attribute\n")
male_radio=driver.find_element(By.CSS_SELECTOR,"input[id='male']")
male_radio.click()
print("Successfully located Male radio button using Attribute Selector")
time.sleep(2)

print("\n4. CSS Wildcard - Starts With (^=)\n")
start_elements = driver.find_elements(By.CSS_SELECTOR, "input[id^='input']")

print("Elements whose ID starts with 'input':", len(start_elements))

for index, element in enumerate(start_elements, start=1):
    print(f"{index}. {element.get_attribute('id')}")

time.sleep(2)


print("\n5. CSS Wildcard Selector - Ends with ($=)\n" )
end_elements = driver.find_elements(By.CSS_SELECTOR, "input[id$='date']")

print("Elements whose ID ends with 'date':", len(end_elements))

for index, element in enumerate(end_elements, start=1):
    print(f"{index}. {element.get_attribute('id')}")

time.sleep(2)


print("\n6. CSS Wildcard - Contains(*=)\n")
contain_elements = driver.find_elements(By.CSS_SELECTOR, "input[id*='date']")

print("Elements whose ID starts with 'input':", len(contain_elements))

for index, element in enumerate(contain_elements, start=1):
    print(f"{index}. {element.get_attribute('id')}")

time.sleep(2)