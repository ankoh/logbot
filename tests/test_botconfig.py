import unittest
import os

from bot.botconfig import BotConfiguration

class TestBotConfiguration(unittest.TestCase):
    default_value='null'

    env_keys = [
        'DB_HOST',
        'DB_PORT',
        'DB_USER',
        'DB_SECRET',
        'SLACK_API_KEY'
    ]
    
    def write_valid_config(self):
        for env_key in self.env_keys:
            os.environ[env_key]='null'

    def run_key_test(self, key):
        self.write_valid_config()
        os.environ.pop(key)
        self.assertFalse(BotConfiguration().is_valid())
        os.environ[key] = self.default_value
        config = BotConfiguration()
        self.assertTrue(config.is_valid())
        self.assertEqual(config.get(key),self.default_value)

    def test_db_host(self):
        self.run_key_test('DB_HOST')

    def test_db_port(self):
        self.run_key_test('DB_PORT')

    def test_db_user(self):
        self.run_key_test('DB_USER')

    def test_db_secret(self):
        self.run_key_test('DB_SECRET')

    def test_db_slack_api_key(self):
        self.run_key_test('SLACK_API_KEY')
