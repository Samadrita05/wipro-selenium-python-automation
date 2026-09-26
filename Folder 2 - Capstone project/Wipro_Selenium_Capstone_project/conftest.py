import pytest

from utilities.config_reader import ConfigReader
from utilities.driver_factory import DriverFactory

@pytest.fixture
def driver():
    config = ConfigReader()
    browser = config.get_browser()

    driver = DriverFactory.get_driver(browser)
    driver.maximize_window()

    yield driver

    driver.quit()
def pytest_html_report_title(report):
    report.title = "Wipro Selenium Automation Test Report"


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "Wipro Selenium Automation Framework"
        config._metadata["Automation"] = "Selenium + Python + PyTest"
        config._metadata["Browser"] = "Chrome"
        config._metadata["Test Suite"] = "Login and Product Search"