import psycopg2
import unittest
import os
from os.path import join, dirname
from bot.pg import PostgresClient
from bot.config import BotConfiguration

project_root = dirname(dirname(__file__))
sql_dir = join(project_root,'sql')
schema_creation_script = join(sql_dir, 'schema_create.sql')
schema_drop_script = join(sql_dir, 'schema_drop.sql')

class TestPostgresClient(unittest.TestCase):

    def prepare_connection(self) -> ():
        """
        Prepares a test databse 
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
        self.prepare_connection()
        self.client.run_script(schema_drop_script)
        self.client.run_script(schema_creation_script)