import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler


log_name = 'server.log'
logger = logging.getLogger(log_name)

# Определяем формат сообщений для логирования
_format = logging.Formatter('%(asctime)s - %(levelname)-10s - %(module)s - %(message)s')

# ежедневная ротация лог файла
rotate_server_log = TimedRotatingFileHandler(
    os.path.join(os.path.dirname(__file__), log_name),
    when='D',
    interval=1,
    encoding='utf-8'
)
rotate_server_log.setLevel(logging.INFO)
rotate_server_log.setFormatter(_format)

logger.addHandler(rotate_server_log)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    logger.info('Тестовый запуск логирования')
