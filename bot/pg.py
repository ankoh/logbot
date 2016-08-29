import psycopg2
from datetime import datetime
from os.path import join, dirname
from bot.config import BotConfiguration

project_root = dirname(dirname(__file__))
sql_dir = join(project_root,'sql')
create_schema_script = join(sql_dir, 'create_schema.sql')
drop_relations_script = join(sql_dir, 'drop_relations.sql')

class PostgresClient(object):
    """
    The Postgres client provides convenience methods
    to manipulate the postgres database
    """
    
    def __init__(self, config: BotConfiguration):
        self.initialized = False
        self.config = config
        self.conn = None

    def connect(self) -> bool:
        """
        Connect to the postgres database
        """
        try:
            self.conn = psycopg2.connect(
                host=self.config.get(BotConfiguration.Settings.PG_HOST),
                port=self.config.get(BotConfiguration.Settings.PG_PORT),
                database=self.config.get(BotConfiguration.Settings.PG_DB),
                user=self.config.get(BotConfiguration.Settings.PG_USER),
                password=self.config.get(BotConfiguration.Settings.PG_SECRET)
            )
            self.initialized = True
            return True
        except psycopg2.OperationalError:
            return False

    def run_script(self, path: str, autocommit = True) -> ():
        """
        Runs a sql script at a given path
        """
        assert self.initialized
        t = self.conn.autocommit
        self.conn.autocommit = autocommit
        with self.conn.cursor() as cursor:
            cursor.execute(open(path, "r").read())
        self.conn.autocommit = t

    def create_schema(self) -> int:
        """
        Creates the sql schema
        """
        self.run_script(create_schema_script)
    
    def drop_relations(self) -> int:
        """
        Drops all relations
        """
        self.run_script(drop_relations_script)
    
    def insert_or_update_profile(self, key: str) -> int:
        """
        Inserts or updates a profile
        """
        sql_string = 'INSERT INTO profile (key) VALUES (%s) ON CONFLICT (key) DO UPDATE SET key=EXCLUDED.key RETURNING id;'
        with self.conn.cursor() as cursor:
            cursor.execute(sql_string,[key])
            self.conn.commit()
            return cursor.fetchone()[0]
    
    def insert_or_update_channel(self, key: str) -> int:
        """
        Inserts or updates a channel
        """
        sql_string = 'INSERT INTO channel (key) VALUES (%s) ON CONFLICT (key) DO UPDATE SET key=EXCLUDED.key RETURNING id;'
        with self.conn.cursor() as cursor:
            cursor.execute(sql_string,[key])
            self.conn.commit()
            return cursor.fetchone()[0]

    def insert_channel_message(self, channel: str, profile: str, content: str, clock: str) -> ():
        """
        Inserts or updates a channel message
        """
        profile_id = self.insert_or_update_profile(profile)
        channel_id = self.insert_or_update_channel(channel)
        sql_string = 'INSERT INTO channel_message (author, channel, received,  clock, content) VALUES (%s, %s, %s, %s, %s);'
        with self.conn.cursor() as cursor:
            cursor.execute(sql_string,[profile_id, channel_id, datetime.now(), clock, content])
            self.conn.commit()
