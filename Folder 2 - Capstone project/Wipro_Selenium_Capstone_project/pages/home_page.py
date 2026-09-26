from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.search_box = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def enter_search_text(self, product):
        self.driver.find_element(*self.search_box).send_keys(product)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()