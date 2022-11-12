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
    s = str(data)[2:-1]
    dict_of_answer = {'Hello!': 'Hi!', 'How are you?': 'I am fine, because I am just a server!',
                      'What are you doing now?': 'I am computing smth...',
                      'Goodbye': 'See you later'}
    if s in dict_of_answer.keys():
        message = dict_of_answer[s]
    else:
        message = input('Enter message')
    conn.send(bytes(message, encoding='UTF-8'))
conn.close()
