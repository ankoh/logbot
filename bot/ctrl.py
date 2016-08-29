from bot.rtm import RTMClient
from bot.pg import PostgresClient
from bot.logging import log
from rx.core import Observer
from pprint import pprint

class BotController(Observer):
    """
    As the behavior of the bot is quite straight forward we
    will use a single controller that subscribes the rtm client
    and uses the pg client to write to the database
    """

    def __init__(self, rtm_client:RTMClient, pg_client: PostgresClient):
        self.rtm_client = rtm_client
        self.pg_client = pg_client
        self.rtm_client.incoming_data.subscribe(observer=self)

    def on_next(self, data):
        """
        rx.Observer's next handler
        """
        if 'type' not in data: return
        ty = data['type']
        if ty == 'message':
            self.handle_message(data)
        else:
            log.debug('Untracked type "{0}"'.format(ty))

    def on_error(self, error):
        """
        rx.Observer's error handler
        """
        pass

    def on_completed(self, error):
        """
        rx.Obsvers's completion handler
        """
        pass

    def handle_message(self, data):
        """
        Handles all data with 'type':'message'
        """

        # TODO: For now we only support pure messages
        # Subtypes like 'message_changed' etc. are dropped
        if 'subtype' in data:
            log.debug('Untracked message subtype "{0}"'.format(data['subtype']))

        # Check fields
        if 'channel' not in data: return
        if 'user' not in data: return
        if 'ts' not in data: return
        if 'text' not in data: return

        # Write to database
        self.pg_client.insert_channel_message(data['channel'],data['user'],data['text'],data['ts']) 
        log.debug('Received message in channel "{0}" of user "{1}"'.format(data['channel'],data['user']))
