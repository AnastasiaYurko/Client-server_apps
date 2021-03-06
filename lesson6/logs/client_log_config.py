import inspect
import logging
import os
import sys

log_name = 'client.log'
logger = logging.getLogger(log_name)

_format = logging.Formatter('%(asctime)s - %(levelname)-10s - %(module)s - %(message)s')

client_log = logging.FileHandler(os.path.join(os.path.dirname(__file__), log_name), encoding='utf-8')
client_log.setLevel(logging.INFO)
client_log.setFormatter(_format)

client_stream = logging.StreamHandler(sys.stdout)
client_stream.setLevel(logging.INFO)
client_stream.setFormatter(_format)

logger.addHandler(client_log)
logger.setLevel(logging.INFO)
logger.addHandler(client_stream)
logger.setLevel(logging.INFO)


if __name__ == '__main__':

    print(inspect.stack())
    print(inspect.stack()[2][3])
