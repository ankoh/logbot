import psycopg2
from bot.config import BotConfiguration

class PostgresClient(object):
    """
    The Postgres writer maintains a connection to a postgres database.
    """
    
    def __init__(self, config: BotConfiguration, existing_conn = None):
        if connection is None:
            self.config = config
            self.initialized = False
        else:
            self.initialized = True
            self.conn = existing_conn
            self.config = None
    
    def connect() -> Bool:
        """
        Connect to the postgres database
        """
        try:
            self.conn=psycopg2.connect(
                host=config.get(BotConfiguration.Settings.PG_HOST),
                port=config.get(BotConfiguration.Settings.PG_PORT),
                database=config.get(BotConfiguration.Settings.PG_DB),
                profile=config.get(BotConfiguration.Settings.PG_profile),
                password=config.get(BotConfiguration.Settings.PG_SECRET)
            )
            self.initialized = True
            return True
        except psycopg2.OperationalError:
            return False

    def run_schema(schema_file: str):
        """
        Run the schema file against the database
        """
        assert self.initialized
        

    