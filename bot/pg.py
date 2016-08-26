import psycopg2
from bot.config import BotConfiguration

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
    
