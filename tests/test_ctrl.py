import unittest
import os
from bot.config import BotConfiguration
from bot.rtm import RTMClient
from bot.ctrl import BotController

class TestBotController(unittest.TestCase):
    def test_ctrl_init(self) -> ():
        config = BotConfiguration()
        rtm_client = RTMClient(config)
        controller = BotController(rtm_client,None)
