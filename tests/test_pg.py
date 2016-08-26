import psycopg2
import unittest
import os
from os.path import join, dirname

project_root = dirname(dirname(__file__))
sql_dir = join(project_root,'sql')
schema_creation_script = join(sql_dir, 'schema_create.sql')
schema_drop_script = join(sql_dir, 'schema_drop.sql')

class TestPostgresClient(unittest.TestCase):
    def prepare_test_db(self):
        try:
            self.conn=psycopg2.connect(
                host='postgres',
                port=5432,
                database='logbot_testdb',
                user='logbot_test_runner',
                password='thanks_for_all_the_fish'
            )
            self.clean_test_db();
        except psycopg2.OperationalError:
            raise unittest.SkipTest('Could not connect to test database')

    def clean_test_db(self):
        """
        Cleans the test database
        """
        t = self.conn.autocommit
        self.conn.autocommit = True
        with self.conn.cursor() as cursor:
            cursor.execute(open(schema_drop_script, "r").read())
        self.conn.autocommit = t

    def schema_creation_test(self):
        """
        Tests if the schema is valid
        """
        t = self.conn.autocommit
        self.conn.autocommit = True
        with self.conn.cursor() as cursor:
            cursor.execute(open(schema_creation_script, "r").read())
        self.conn.autocommit = t

    def test_db_interaction(self):
        """
        Prepares a test databse and runs tests agains it
        TODO: A custom ordered test suite would probably be much nice
        """
        self.prepare_test_db()
        self.schema_creation_test()