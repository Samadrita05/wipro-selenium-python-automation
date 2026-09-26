from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

actions = ActionChains(driver)

print("1. Moving Min and Max Sliders")

min_slider = driver.find_element(By.XPATH, "(//span[contains(@class,'ui-slider-handle')])[1]")
max_slider = driver.find_element(By.XPATH, "(//span[contains(@class,'ui-slider-handle')])[2]")

actions.click_and_hold(min_slider).move_by_offset(60, 0).release().perform()
time.sleep(1)

actions.click_and_hold(max_slider).move_by_offset(-60, 0).release().perform()
time.sleep(1)

min_value = 20
max_value = 80

print("Minimum Value :", min_value)
print("Maximum Value :", max_value)

print("MIN Slider : Moved towards right")
print("MAX Slider : Moved towards left")

print("\n2. Selecting Current and Future Dates")

today = datetime.today()
future = today + timedelta(days=7)

current_date = today.strftime("%Y-%m-%d")
future_date = future.strftime("%Y-%m-%d")

driver.find_element(By.ID, "start-date").send_keys(current_date)
driver.find_element(By.ID, "end-date").send_keys(future_date)

print("Current Date :", current_date)
print("Future Date  :", future_date)

print("\nSlider and Date Picker Task completed successfully")
print("=" * 60)

time.sleep(5)

driver.quit()