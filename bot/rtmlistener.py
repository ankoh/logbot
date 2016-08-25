
from bot.botconfig import BotConfiguration
from slackclient import SlackClient

class RTMListener(object):
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

    def connect(self):
        assert !self.initialized
        self.client = SlackClient(config.get(BotConfiguration.Settings.SLACK_API_KEY))
    
    pass


