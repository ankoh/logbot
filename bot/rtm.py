from bot.config import BotConfiguration
from bot.logging import log
from slackclient import SlackClient
from rx.subjects import Subject

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
        self.incoming_events = Subject()

    def connect(self) -> bool:
        """
        Connect to the RTM API
        """
        assert not self.initialized
        if not self.client.rtm_connect():
            return False
        self.initialized = True       
        return True

    def autoping(self):
        """
        Ping the server every 3 seconds
        """
        assert self.initialized
        now = int(time.time())
        if now > self.last_ping + 3:
            self.client.server.ping()
            self.last_ping = now

    def run(self):
        """
        Connects the client to the Slack RTM API and publishes events
        to the incoming_events subject

        Note that this client is meant to run in the foreground.
        The subscribers then use incoming_events.subscribeOn(...) to
        schedule their callbacks with an asynchronous scheduler.
        """
        log.info("Connecting to the Slack API")
        if not self.connect():
            log.critical("Failed to connect to the Slack API")
            return
        
        while True:
            for reply in self.client.rtm_read():
                self.incoming_events.onNext(reply)
            self.autoping()
            time.sleep(.1)

        