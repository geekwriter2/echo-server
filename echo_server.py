"""
Python 230 Lesson2: echo-server
"""

import socket
import sys
# pylint: disable=C0103
# pylint: disable=R0101

BUFFER_SIZE = 16


def server(log_buffer=sys.stderr):
    """server connection """

    # set an address for our server
    address = ('127.0.0.1', 10000)
    sock = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)
    sock.listen()
    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()
            try:
                while True:
                    print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                    data = conn.recv(BUFFER_SIZE)
                    print("Client says: {}".format(data.decode('utf8')))

                    conn.send(data)

                    if len(data) < 16:
                        print('sent {0}'.format(data.decode('utf8')))
                        break
            except ConnectionError as e:
                print(e)
                sys.exit(1)
            finally:
                conn.close()
                print('connection closed', file=log_buffer)
    except KeyboardInterrupt:
        print('quitting echo server', file=log_buffer)
        sys.exit(1)


if __name__ == '__main__':
    server()
    sys.exit(0)
