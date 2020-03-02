import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 31000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)
print(sys.stderr, 'waiting for a connection')
connection, client_address = sock.accept()
print(sys.stderr, 'connection from', client_address)
data = connection.recv(64).decode()
print(sys.stderr, 'received "%s"' % data)
filenya = open('hasil.txt','w')
print('Processing to file..')
filenya.write(data)
connection.close()