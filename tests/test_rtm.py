import unittest
import os
from bot.config import BotConfiguration
from bot.rtm import RTMClient

class TestRTMClient(unittest.TestCase):
    def write_valid_config(self):
        for key in BotConfiguration.Settings:
            os.environ[key.name]='null'

    def test_rtm_init(self):
        self.write_valid_config()
        client = RTMClient(BotConfiguration())
