from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

# Print page title
print("=" * 60)
print("Assignment 2 - Multiple Element Identification")
print("=" * 60)
print("Page Title :", driver.title)
print("=" * 60)

print("\n1. Finding all INPUT ELEMENTS\n")

input_elements =driver.find_elements(By.TAG_NAME, "input")

print("Total number of input elements:", len(input_elements))
print("-" * 60)

# demonstrating input elements
for index, element in enumerate(input_elements, start=1):
    element_id = element.get_attribute("id") or "Not Available"
    element_name = element.get_attribute("name") or "Not Available"
    element_type = element.get_attribute("type") or "Not Available"

    print(f"Input {index}")
    print(f"ID   : {element_id}")
    print(f"Name : {element_name}")
    print(f"Type : {element_type}")
    print("-" * 60)

time.sleep(2)

print("\n2. Finding all hyperlinks\n")

links = driver.find_elements(By.TAG_NAME, "a")

print("Total hyperlinks found:", len(links))
print("-" * 60)

for index, link in enumerate(links, start=1):

    link_text = link.text.strip()

    if link_text == "":
        link_text = "(No Visible Text)"

    print(f"Link {index}: {link_text}")

print("-" * 60)
time.sleep(2)

print("\n3. Finding all Buttons\n")
buttons = driver.find_elements(By.TAG_NAME, "button")
print("Total buttons found:", len(buttons))
print("-" * 60)
for index, button in enumerate(buttons, start=1):
    button_text = button.text.strip()

    if button_text == "":
        button_text = "(No Visible Text)"

    print(f"Button {index}: {button_text}")
print("-" * 60)
time.sleep(2)