import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portnum = int(input('Input port number(31000):'))
server_address = ('localhost', portnum)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
filenya = open('file.txt','r')
message = (filenya.read())
print(sys.stderr, 'sending "%s"' % message)
sock.sendall(message.encode())
print(sys.stderr, 'closing socket')
sock.close()

