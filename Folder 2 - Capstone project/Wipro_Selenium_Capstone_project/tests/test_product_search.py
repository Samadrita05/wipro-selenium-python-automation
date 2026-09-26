import unittest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utilities.config_reader import ConfigReader
from utilities.csv_reader import CSVReader
from utilities.driver_factory import DriverFactory
from utilities.screenshot import ScreenshotUtility

class TestProductSearch(unittest.TestCase):

    def test_product_search(self):
        config = ConfigReader()
        test_data = CSVReader.read_test_data()[0]

        driver = DriverFactory.get_driver(config.get_browser())
        driver.maximize_window()

        try:
            driver.get(config.get_application_url())

            home_page = HomePage(driver)

            home_page.enter_search_text(test_data["product"])
            home_page.click_search()

            search_page = SearchPage(driver)
            results = search_page.get_search_results()

            self.assertGreater(len(results), 0)

        except Exception:
            ScreenshotUtility.capture(driver, "test_product_search")
            raise

        finally:
            driver.quit()