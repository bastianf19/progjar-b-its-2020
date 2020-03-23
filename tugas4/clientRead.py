import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_num = 8081
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1", " Port:", port_num)
sock.connect(server_address)

try:
    namafile = 'tes.txt'
    filenya = open(namafile,'rb')
    baca = filenya.read()
    baca = baca.decode()
    pesan = 'add '+namafile+' '+baca
    sock.send(pesan.encode())

    data = sock.recv(2048).decode()
    print(data)

finally:
    print('Close Connection')
    sock.close()