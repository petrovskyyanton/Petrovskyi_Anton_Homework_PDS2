import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
a = input('Number A:')
b = input('Number B:')
r = f'{a} {b}'
sock.send(bytes(str(r), encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data.decode('UTF-8'))
