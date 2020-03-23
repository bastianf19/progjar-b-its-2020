import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_num = 8081
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1", " Port:", port_num)
sock.connect(server_address)

try:
    namafile = 'teks1.txt'
    pesan = str('get '+namafile)
    sock.send(pesan.encode())

    datanya = sock.recv(4096)
    filenya = open(namafile,'wb')
    filenya.write(datanya)
    filenya.close()

finally:
    print('File sukses diambil')
    print('Close Connection')
    sock.close()