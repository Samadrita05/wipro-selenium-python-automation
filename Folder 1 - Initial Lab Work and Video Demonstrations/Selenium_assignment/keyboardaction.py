from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://text-compare.com/")
time.sleep(3)

print("=" * 60)
print("Assignment - Keyboard Actions")
print("=" * 60)

left_box = driver.find_element(By.ID, "inputText1")
right_box = driver.find_element(By.ID, "inputText2")

actions = ActionChains(driver)

left_box.click()
actions.send_keys("Welcome to Selenium").perform()
time.sleep(2)

actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(1)

actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(1)

right_box.click()
time.sleep(1)

actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(2)

print("Text entered in left text box successfully.")
print("Text copied successfully.")
print("Text pasted into right text box successfully.")

print("=" * 60)
print("Assignment completed successfully.")
print("=" * 60)

time.sleep(3)
driver.quit()