import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            break


if __name__ == '__main__':
    start_client()
