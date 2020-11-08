import socket


class Sock(socket.socket):
    def __init__(self, is_server: bool):
        super(Sock, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.__set_status(is_server)

    def __set_status(self, is_server: bool):
        self.bind(('127.0.0.1', 1234)) if is_server else self.connect(('127.0.0.1', 1234))

    def listen_socks(self, user: socket.socket):
        raise NotImplemented

    def send_data(self, where, data, current):
        raise NotImplemented
