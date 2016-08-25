import unittest
import os
from bot.botconfig import BotConfiguration
from bot.rtmclient import RTMClient

class TestRTMClient(unittest.TestCase):
    def write_valid_config(self):
        for key in BotConfiguration.Settings:
            os.environ[key.name]='null'

    def test_init(self):
        self.write_valid_config()
        client = RTMClient(BotConfiguration())
