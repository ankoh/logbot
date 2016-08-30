import argparse
import sys
import time
from os.path import isfile,join
from bot.logging import log
from bot.config import BotConfiguration
from bot.pg import PostgresClient
from bot.rtm import RTMClient
from bot.ctrl import BotController

def main() -> ():
    # Prepare argument parser
    arg_parser=argparse.ArgumentParser(description="Logbot runner")
    arg_parser.add_argument('-t', '--target', type=str, default=['bot'], nargs=1, help='Execution mode')
    args = arg_parser.parse_args();

    # Read environment
    config = BotConfiguration()
    if not config.is_valid():
        log.critical('Invalid or missing environment variable "' + config.blame + '"')

    # Create postgres client
    retries = 5
    pg_client = PostgresClient(config)
    while retries > 0:
        if pg_client.connect():
            break
        log.info("Couldn't reach Postgres. Sleeping a bit..")
        retries -= 1
        time.sleep(1)

    if retries == 0:
        log.critical("Giving up! Failed to connect to postgres database")

    # Run the different modes
    if args.target[0]=='prepare':
        pg_client.create_schema()
        log.info("Created SQL Schema")

    elif args.target[0]=='bot':
        rtm_client = RTMClient(config)
        controller = BotController(rtm_client,pg_client)
        rtm_client.run_loop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

