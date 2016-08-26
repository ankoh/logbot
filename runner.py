import argparse
import sys
from os.path import isfile,join
from bot.logging import log
from bot.config import BotConfiguration
from bot.pg import PostgresClient
from bot.rtm import RTMClient

def main() -> ():
    # Prepare argument parser
    arg_parser=argparse.ArgumentParser(description="Logbot runner")
    arg_parser.add_argument('-m', '--mode', type=str, default='bot', nargs=1, help='Execution mode')
    args = arg_parser.parse_args();

    # Read environment
    config = BotConfiguration()
    if not config.is_valid():
        log.critical('Invalid or missing environment variable "' + config.blame + '"')

    # Create postgres client
    pg_client = PostgresClient(config)
    if not pg_client.connect():
        log.critical("Failed to connect to postgres database")
        return

    # Run the different modes
    if args.mode[0]=='prepare':
        pg_client.create_schema()
        log.info("Created SQL Schema")
    elif args.mode[0]=='bot':
        rtm = RTMClient(config)
        rtm.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    