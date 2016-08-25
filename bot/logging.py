import logging
import sys

def create_logger():
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger('logbot')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

log = create_logger()