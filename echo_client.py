"""
Python 230, Lesson2: echo_client
"""

import socket
import sys
# pylint: disable=C0103
# pylint: disable=W0150

SERVER_ADDRESS = ('127.0.0.1', 10000)


def client(msg, log_buffer=sys.stderr):
    """create a client connection"""

    received_message = ''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to {0} port {1}'.format(*SERVER_ADDRESS), file=log_buffer)
    sock.connect(SERVER_ADDRESS)
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(msg.encode('utf-8'))
        while True:
            chunk = sock.recv(16)
            received_message += chunk.decode('utf8')
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            if len(chunk) < 16:
                break
    except ConnectionError as e:
        print(e)
        sys.exit(1)
    finally:
        print('closing socket', file=log_buffer)
        sock.close()
        return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    message = sys.argv[1]
    print(client(message))
