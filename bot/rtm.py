from bot.config import BotConfiguration
from bot.logging import log
from slackclient import SlackClient
from rx.subjects import Subject
from bot.logging import log
import time

class RTMClient(object):
    """
    The RTMListener maintains a WebSocket to the Slack RTM API and
    forwards any incoming data via ReactiveX Observables.

    Read this for more information on ReactiveX:
    http://reactivex.io/documentation/observable.html
    """
    
    def __init__(self, config: BotConfiguration):
        self.config = config
        self.client = None
        self.initialized = False
        self.last_ping = 0
        self.client = SlackClient(config.get(BotConfiguration.Settings.SLACK_API_KEY))
        self.incoming_data = Subject()

    def connect(self) -> bool:
        """
        Connect to the RTM API
        """
        assert not self.initialized
        if not self.client.rtm_connect():
            return False
        self.initialized = True       
        return True

    def autoping(self) -> ():
        """
        Ping the server every 3 seconds
        """
        assert self.initialized
        now = int(time.time())
        if now > self.last_ping + 3:
            log.debug("Ping")
            self.client.server.ping()
            self.last_ping = now

    def run(self, infinite_loop = True) -> ():
        """
        Connects the client to the Slack RTM API and publishes events
        to the incoming_data subject

        Note that this client is meant to run in the foreground.
        The subscribers then use incoming_data.subscribeOn(...) to
        schedule their callbacks with an asynchronous scheduler.
        """
        assert not self.initialized
        log.debug('Connecting to the Slack API')
        if not self.connect():
            log.critical('Failed to connect to the Slack API')
            return
        log.info('Established connection to the Slack API')
        
        first_run = True
        while infinite_loop or first_run:
            for reply in self.client.rtm_read():
                log.debug('Received: ' + str(reply))
                self.incoming_data.on_next(reply)
            self.autoping()
            if not first_run:
                time.sleep(.1)
            first_run = False

        