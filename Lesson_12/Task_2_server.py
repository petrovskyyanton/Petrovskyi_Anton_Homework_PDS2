import asyncio
import socket


async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(client, 1024)).decode('utf8')
        global s
        s = request.split(' ')
        await r1()
        await r2()
        await r3()
        answer = f'A+B={r1}; A-B={r2}; A*B={r3}'
        await loop.sock_sendall(client, answer.encode('utf8'))
        break
    client.close()


async def r1():
    global r1
    r1 = int(s[0]) + int(s[1])
    await asyncio.sleep(2)
    print(f'A+B={r1}')


async def r2():
    global r2
    r2 = int(s[0]) - int(s[1])
    await asyncio.sleep(2)
    print(f'A-B={r2}')


async def r3():
    global r3
    r3 = int(s[0]) * int(s[1])
    await asyncio.sleep(2)
    print(f'A*B={r3}')


async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 55000))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))


asyncio.run(run_server())
