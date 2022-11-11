import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 56000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    dict_of_answer = {b'Hello!': 'Hi!', b'How are you?': 'I am fine, because I am just a server!',
                      b'What are you doing now?': 'I am computing smth...'}
    if data in dict_of_answer.keys():
        message = dict_of_answer[data]
    else:
        message = input('Enter message')
    conn.send(bytes(message, encoding='UTF-8'))
conn.close()
