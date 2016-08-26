import psycopg2
import unittest
import os

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
        except psycopg2.OperationalError:
            raise unittest.SkipTest('Could not connect to test database')

    def run_schema_test(self):
        pass

    def test_db_interaction(self):
        self.prepare_test_db()
        self.run_schema_test()