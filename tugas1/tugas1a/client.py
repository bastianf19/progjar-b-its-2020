import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 31000)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
filenya = open('file.txt','r')
message = (filenya.read())
print(sys.stderr, 'sending "%s"' % message)
sock.sendall(message.encode())
print(sys.stderr, 'closing socket')
sock.close()
