from threading import Thread
import socket
from Sock import Sock


class Server(Sock):
    def __init__(self):
        super(Server, self).__init__(is_server=True)
        self.__users = []
        self.listen()

    def start_server(self):
        while True:
            user_socket, address = self.accept()
            self.__users.append(user_socket)

            listen_accepted_usr = Thread(target=self.__listen_socks, args=([user_socket]))
            listen_accepted_usr.start()

            print(f'Подключился {address[0]}')

    @staticmethod
    def __send_data(where, data, current=None):
        for user in where:
            user.send(data) if user != current else ...

    def __listen_socks(self, user):
        while True:
            data = user.recv(1024)
            print(f'{user.getsockname()}: {data.decode("utf-8")}')
            self.__send_data(where=self.__users, data=data, current=user)


"""server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        except Exception:
            server.close()
            break"""


if __name__ == '__main__':
    s = Server()
    s.start_server()
