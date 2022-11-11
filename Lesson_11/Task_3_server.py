import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 57000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    s = str(data)[2:-1]
    print(s)
    number_of_words = len(s.split(' '))
    conn.send((bytes(str(number_of_words), encoding='UTF-8')))
conn.close()