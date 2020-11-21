import socket
# cd C:\Users\mimcdona\Dropbox\UW\UW-Python230_Project\echo-server\echo-server
# python hello_world_server.py
"""
hadron_socket = socket.getaddrinfo('hasthelargehadroncolliderdestroyedtheworldyet.com', 'http')
print(hadron_socket)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
client.connect(('216.92.96.71', 80))
msg = "GET / HTTP/1.1\r\n"
msg += "Host: hasthelargehadroncolliderdestroyedtheworldyet.com\r\n\r\n"
# You can only send bytes through a socket, never unicode:
msg = msg.encode('utf8')
print(msg)

client.sendall(msg)
response = client.recv(1028)
print(response)

# always manually clos sockets
client.close()
"""

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
server_socket.bind(('127.0.0.1', 50002))
server_socket.listen()
connection, client_address = server_socket.accept()
with connection:
    print('Connected by', client_address)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
