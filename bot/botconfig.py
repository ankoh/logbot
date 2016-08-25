import os
from enum import Enum

class BotConfiguration:
    """
    The BotConfiguration object holds the configuration of the logbot
    In order to simplify the distribution as Docker image it will read
    the settings from environment variables.
    """

    class Settings(Enum):
        DB_HOST = 1
        DB_PORT = 2
        DB_USER = 3
        DB_SECRET = 4
        SLACK_API_KEY = 5

    def __init__(self):
        self.valid = True
        self.config = {}
        for key in BotConfiguration.Settings:
            self.assert_env(key.name)

    def assert_env(self, key):
        self.valid &= key in os.environ
        if self.valid:
            self.config[key] = os.environ[key]

    def is_valid(self):
        return self.valid

    def get(self,key):
        assert self.is_valid()
        return self.config[key]

