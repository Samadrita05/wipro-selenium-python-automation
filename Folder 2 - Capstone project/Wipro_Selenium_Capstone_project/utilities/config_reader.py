import configparser
import os

class ConfigReader:
    def __init__(self):
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.ini"
        )

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_application_url(self):
        return self.config["application"]["url"]

    def get_login_url(self):
        return self.config["application"]["login_url"]

    def get_browser(self):
        return self.config["application"]["browser"]