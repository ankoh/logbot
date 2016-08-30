import psycopg2
import unittest
import os
from datetime import datetime
from bot.pg import PostgresClient
from bot.config import BotConfiguration

class TestPostgresClient(unittest.TestCase):

    def prepare_connection(self) -> ():
        """
        Prepares a connection to the test database 
        """
        os.environ[BotConfiguration.Settings.PG_HOST.name] = 'postgres'
        os.environ[BotConfiguration.Settings.PG_PORT.name] = '5432'
        os.environ[BotConfiguration.Settings.PG_DB.name] = 'logbot_testdb'
        os.environ[BotConfiguration.Settings.PG_USER.name] = 'logbot_test_runner'
        os.environ[BotConfiguration.Settings.PG_SECRET.name] = 'thanks_for_all_the_fish'
        os.environ[BotConfiguration.Settings.SLACK_API_KEY.name] = 'null'

        self.config = BotConfiguration()
        self.assertTrue(self.config.is_valid())
        self.client = PostgresClient(self.config)

        try:
            self.client.connect()
        except psycopg2.OperationalError:
            raise unittest.SkipTest('Could not connect to test database')

    def test_postgres_client(self) -> ():
        """
        Tests the postgres client
        """

        # Prepare database
        self.prepare_connection()
        self.client.drop_relations()
        self.client.create_schema()

        # Insert a bunch of messages
        self.client.insert_message('C2147483705', 'U2147483697', 'Hello world', 'clock')
        self.client.insert_message('C2147483705', 'U2147483697', '.', 'clock')
