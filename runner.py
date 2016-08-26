import argparse
import sys
from os.path import isfile,join
from bot.logging import log
from bot.config import BotConfiguration
from bot.pg import PostgresClient

project_root=dirname(dirname(__file__))
default_schema=join(project_root,'schema.sql')

def main() -> ():
    # Prepare argument parser
    arg_parser=argparse.ArgumentParser(description="Logbot runner")
    arg_parser.add_argument('-m', '--mode', type=str, default='bot', nargs=1, help='Execution mode')
    args = arg_parser.parse_args();

    # Read environment
    config = BotConfiguration()
    if not config.is_valid():
        log.critical('Invalid or missing setting "' + config.blame + '"')

    # Create postgres client
    pg_client = PostgresClient(config)
    if not pg_client.connect():
        log.critical("Failed to connect to postgres database")
        return

    # Run the different modes
    if args.mode[0]=='prepare':
        
        pass

    if args.mode[0]=='bot':
        pass


if __main__ == '__main__':
    main()
    