import os
from enum import Enum

class BotConfiguration:
    """
    The BotConfiguration object holds the configuration of the logbot
    In order to simplify the distribution as Docker image it will read
    the settings from environment variables.
    """

    class Settings(Enum):
        PG_HOST = 1
        PG_PORT = 2
        PG_USER = 3
        PG_SECRET = 4
        PG_DB = 5
        SLACK_API_KEY = 6

    def __init__(self):
        self.valid = True
        self.config = {}
        self.blame = ''
        for key in BotConfiguration.Settings:
            self.assert_env(key.name)
            if not self.valid:
                self.blame=key.name
                break

    def assert_env(self, key) -> bool:
        self.valid &= key in os.environ
        if self.valid:
            self.config[key] = os.environ[key]

    def is_valid(self) -> bool:
        return self.valid

    def get(self,setting):
        assert self.is_valid()
        return self.config[setting.name]

