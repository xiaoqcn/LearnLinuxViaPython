import sys
import socket
import time
import traceback


def main(jj):
    print(1)
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(2)
    socket_client.connect(("127.0.0.1", 19999))
    print(3)
    socket_client.sendall(b'client')
    print(4)
    data = socket_client.recv(1024)
    print(5, data)
    # _remote_info = socket_client.getpeername()
    # _local_info = socket_client.getsockname()
    # sock_opt = socket_client.getsockopt()
    # print(_remote_info, _local_info)
    # print(data, socket_client.fileno(), file=sys.stderr)
    # time.sleep(6)
    # socket_client.close()


if __name__ == "__main__":
    for i in range(65535):
        try:
            print('====', i)
            main(i)
        except Exception as ex:
            print(i, ex)
            traceback.print_exc()
            # break
