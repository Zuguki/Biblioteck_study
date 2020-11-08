import socket
from threading import Thread
from Sock import Sock


class Client(Sock):
    def __init__(self):
        super(Client, self).__init__(is_server=False)

    def start_client(self):
        takes = Thread(target=self.__catch_message)
        takes.start()
        while True:
            try:
                self.send(input(': ').encode('utf-8'))
            except Exception:
                self.close()
                break

    def __catch_message(self):
        while True:
            data = self.recv(1024)
            print('-> ', data.decode('utf-8'))
            print(':', end=' ')

    def __send_data(where, data, current=None): ...

    def __listen_socks(self, user): ...


"""client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1243))


def catch_message():
    while True:
        data = client.recv(1024)
        print('-> ', data.decode('utf-8'))
        print(':', end=' ')


def start_client():
    takes = Thread(target=catch_message)
    takes.start()
    while True:
        try:
            client.send(input(': ').encode('utf-8'))
        except Exception:
            client.close()
            break"""


if __name__ == '__main__':
    c = Client()
    c.start_client()
