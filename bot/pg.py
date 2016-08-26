import psycopg2
from bot.config import BotConfiguration

class PostgresClient(object):
    """
    The Postgres writer maintains a connection to a postgres database.
    """
    
    def __init__(self, config: BotConfiguration):
        self.config = config
        self.initialized = False
    
    def connect():
        """
        Connect to the postgres database
        """
        self.conn=psycopg2.connect(
            host=config.get(BotConfiguration.Settings.PG_HOST),
            port=config.get(BotConfiguration.Settings.PG_PORT),
            db=config.get(BotConfiguration.Settings.PG_DB),
            user=config.get(BotConfiguration.Settings.PG_USER),
            secret=config.get(BotConfiguration.Settings.PG_SECRET)
        )
        self.initialized = True

    