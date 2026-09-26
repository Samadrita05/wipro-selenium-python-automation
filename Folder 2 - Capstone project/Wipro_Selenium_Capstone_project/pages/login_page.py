from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.email_field = (By.ID, "input-email")
        self.password_field = (By.ID, "input-password")
        self.login_button = (By.CSS_SELECTOR, "input[value='Login']")

    def enter_email(self, email):
        email_input = self.wait.until(
            EC.visibility_of_element_located(self.email_field)
        )
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.password_field)
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()

    def is_logged_in(self):
        try:
            self.wait.until(
                EC.url_contains("route=account/account")
            )
            return True
        except:
            return False