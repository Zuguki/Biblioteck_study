import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 1243))
server.listen()

while True:
    user_socket, address = server.accept()
    user_socket.send('Welcome'.encode('utf-8'))

    print(f'Подключился {address}')

    data = user_socket.recv(1024)
    print(data.decode('utf-8'))
