from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser.lower() == "chrome":
            return webdriver.Chrome()

        raise ValueError(f"Unsupported browser: {browser}")