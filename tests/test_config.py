import unittest
import os
from bot.config import BotConfiguration

class TestBotConfiguration(unittest.TestCase):
    default_value='null'
    
    def write_valid_config(self) -> ():
        for key in BotConfiguration.Settings:
            os.environ[key.name]='null'

    def test_env_settings(self) -> ():
        for key in BotConfiguration.Settings:
            self.write_valid_config()
            os.environ.pop(key.name)
            self.assertFalse(BotConfiguration().is_valid())
            os.environ[key.name] = self.default_value
            config = BotConfiguration()
            self.assertTrue(config.is_valid())
            self.assertEqual(config.get(key),self.default_value)
