import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portnum = int(input('Input port number(default 31000):'))
server_address = ('localhost', portnum)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
namafile = input('Filename Input + ext:')
namafile = namafile.strip('\n')
message = str(namafile)
print(sys.stderr, 'sending "%s"' % message)
sock.sendall(message.encode())
datafile = sock.recv(100000)
print('datanya: ', datafile)
print('saving to file..')
filenya = open('hasil'+namafile,'wb')
filenya.write(datafile)
print(sys.stderr, 'closing socket')
sock.close()