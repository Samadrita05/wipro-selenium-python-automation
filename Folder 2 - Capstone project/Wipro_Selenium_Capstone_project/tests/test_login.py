import unittest
from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.csv_reader import CSVReader
from utilities.driver_factory import DriverFactory
from utilities.screenshot import ScreenshotUtility

class TestLogin(unittest.TestCase):

    def test_login(self):
        config = ConfigReader()
        test_data = CSVReader.read_test_data()[0]

        driver = DriverFactory.get_driver(config.get_browser())
        driver.maximize_window()

        try:
            driver.get(config.get_login_url())

            login_page = LoginPage(driver)

            login_page.enter_email(test_data["username"])
            login_page.enter_password(test_data["password"])
            login_page.click_login()

            self.assertTrue(
                login_page.is_logged_in(),
                "Login was not successful."
            )

        except Exception:
            ScreenshotUtility.capture(driver, "test_login")
            raise

        finally:
            driver.quit()