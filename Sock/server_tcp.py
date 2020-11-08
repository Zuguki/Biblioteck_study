from threading import Thread
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 1243))
server.listen()

users = []


def send_all(current_user, data):
    for user in users:
        user.send(data) if user != current_user else ...


def listen_user(user: socket.socket):
    while True:
        data = user.recv(1024)
        print(f'{user.getsockname()}: {data.decode("utf-8")}')
        send_all(user, data)


def start_server():
    while True:
        try:
            user_socket, address = server.accept()
            users.append(user_socket)

            listen_accepted_usr = Thread(target=listen_user, args=([user_socket]))
            listen_accepted_usr.start()

            print(f'Подключился {address[1]}')
        except:
            server.close()
            break


if __name__ == '__main__':
    start_server()
