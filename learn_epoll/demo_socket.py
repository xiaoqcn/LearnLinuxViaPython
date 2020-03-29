#! /usr/bin/env python3

import socket
import time
import datetime


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    socket_server_address = ("127.0.0.1", 19999)
    server_socket.bind(socket_server_address)
    server_socket.listen(65535)

    cnt = 0
    # server_socket.setblocking(False)
    while True:
        try:
            connection, address = server_socket.accept()
            # print(connection, address)
            connection.setblocking(False)
            # print(type(connection), connection.fileno())
            cnt += 1
            print(1)
            data = connection.recv(1024)
            print(2)
            peer_name = connection.getpeername()
            # print(peer_name)
            print(3, "ci", data)
            connection.sendall(b"123")
            # time.sleep(7)
            print(4)
            # time.sleep(2)
            connection.close()

        except Exception as ex:
            print("ex", cnt, ex)
            # break


if __name__ == "__main__":
    main()
