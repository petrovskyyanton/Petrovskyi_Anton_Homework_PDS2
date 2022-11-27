import socket
import logging


module_logger = logging.getLogger("log_from.Task_1_server_from_Lesson_11")


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 55000))
    sock.listen(10)
    print('Server is running, please, press ctrl+c to stop')
    while True:
        conn, addr = sock.accept()
        print('connected:', addr)
        data = conn.recv(1024)
        if data.decode() == 'Warning':
            logger = logging.getLogger("log_from.Task_1_server_from_Lesson_11")
            logger.warning(f'Warning! Something wrong!')
        logger = logging.getLogger("log_from.Task_1_server_from_Lesson_11")
        logger.info(f'Message "{data.decode()}" is received from client')
        print(str(data.decode()))
        message = input('Enter message:')
        if message == 'Error':
            logger = logging.getLogger("log_from.Task_1_server_from_Lesson_11")
            logger.error(f'Error detected')
        logger = logging.getLogger("log_from.Task_1_server_from_Lesson_11")
        logger.info(f'Message "{message}" is send from server')
        conn.send(bytes(message, encoding='UTF-8'))

