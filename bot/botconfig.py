import os

class BotConfiguration:
    """
    The BotConfiguration object holds the configuration of the logbot
    In order to simplify the distribution as Docker image it will read
    the settings from environment variables.
    """

    __required_keys = [
        'DB_HOST',
        'DB_PORT',
        'DB_USER',
        'DB_SECRET',
        'SLACK_API_KEY'
    ]

    def __init__(self):
        self.valid = True
        self.config = {}
        for key in self.__required_keys:
            self.assert_env(key)

    def assert_env(self, key):
        self.valid &= key in os.environ
        if self.valid:
            self.config[key] = os.environ[key]

    def is_valid(self):
        return self.valid

    def get(self,key):
        assert self.is_valid()
        return self.config[key]

