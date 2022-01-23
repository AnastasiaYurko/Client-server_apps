from socket import *
from common.config import *
import json
from logs.log import Log
from logs.server_log_config import logger


@Log(logger)
def sendMessageClient(msg):
    return msg.encode(ENCODING)


@Log(logger)
def getMessageClient(msg):
    try:
        msg_ = msg.decode(ENCODING)
        msg = json.loads(msg_)
        if msg['command'] == 'Сервер':
            return 'Привет, клиент'
        elif msg['command'] == 'погода' and msg['text'] == ['Санкт-Петербург']:
            return 'как обычно снег с дождем'
        elif msg['command'] == 'Помощь':
            return '''
        Доступные команды:
            Сервер - отклик сервера
            погода Санкт-Петербург - информация о погоде в СПб
            Помощь - получение справки по доступным командам
    '''
        else:
            return 'введите Помощь чтобы получить справку по командам'
    except:
        logger.error('Ошибка выполнения функции getMessageClient')
        logger.critical('Критическая ошибка выполнения функции getMessageClient')


if __name__ == '__main__':
    tcp = socket(AF_INET, SOCK_STREAM)
    tcp.bind(('', SERVER_PORT))
    tcp.listen(5)

    while True:
        try:
            client, addr = tcp.accept()
            if client:
                logger.info(f'Соединение с {addr[0]} - {addr[1]} установлено')
                logger.debug(f'Соединение с {addr[0]} - {addr[1]} установлено')
                logger.warning(f'Соединение с {addr[0]} - {addr[1]} установлено')


            result = getMessageClient(client.recv(1024))
            client.send(sendMessageClient(result))
            client.close()
        except:
            logger.critical('Критическая ошибка исполнения программы')
            client.send(sendMessageClient('Ошибка на стороне сервера'))
            client.close()
