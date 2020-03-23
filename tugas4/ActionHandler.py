import shelve
import uuid
import os
import socket
import base64

class Action:
    def __init__(self):
        if not os.path.exists("file"):
            os.makedirs("file")

    def get_data(self,nama=None):
        tmp = []
        filenya = open('file/'+nama, 'rb')
        hasilfile = filenya.read()
        # print(hasilfile)
        filenya.close()
        hasilfile = str(hasilfile, 'utf-8')
        return hasilfile

    def add_file(self, filename=None, file=None):
        data_filenya = file
        # print(data_filenya)
        filenya = open("file/"+filename, "wb")
        filenya.write(data_filenya)
        return True

    def list_data(self):
        listnya = os.listdir('file')
        return listnya

if __name__=='__main__':
    act = Action()
    print(act.list_data())