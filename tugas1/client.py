import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portnum = int(input('Input port number(default 31000-31002):'))
server_address = ('localhost', portnum)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print(sys.stderr, 'sending "%s"' % message)
    sock.sendall(message.encode())
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(64).decode()
        amount_received += len(data)
        print(sys.stderr, 'received "%s"' % data)
finally:
    print(sys.stderr, 'closing socket')
    sock.close()
