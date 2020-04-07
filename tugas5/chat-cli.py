import socket
import os
import json

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889


class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP, TARGET_PORT)
        self.sock.connect(self.server_address)
        self.tokenid = ""

    def proses(self, cmdline):
        j = cmdline.split(" ")
        try:
            command = j[0].strip()
            if (command == 'auth'):
                username = j[1].strip()
                password = j[2].strip()
                return self.login(username, password)

            elif (command == 'send'):
                usernameto = j[1].strip()
                message = ""
                for w in j[2:]:
                   message = "{} {}" . format(message, w)
                return self.sendmessage(usernameto, message)

            elif (command == 'inbox'):
                return self.inbox()

            elif (command == 'showuseractive'):
                return self.showuseractive()

            elif (command == 'logout'):
                return self.logout()

            else:
                return "*Maaf, command tidak benar"

        except IndexError:
                return "-Maaf, command tidak benar"

    def sendstring(self, string):
        try:
            self.sock.sendall(string.encode())
            receivemsg = ""
            while True:
                data = self.sock.recv(64)
                print("diterima dari server", data)
                if (data):
                    # data harus didecode agar dapat di operasikan dalam bentuk string
                    receivemsg = "{}{}" . format(receivemsg, data.decode())
                    if receivemsg[-4:] == '\r\n\r\n':
                        print("end of string")
                        return json.loads(receivemsg)
        except:
            self.sock.close()
            return {'status': 'ERROR', 'message': 'Gagal'}

    def login(self, username, password):
        string = "auth {} {} \r\n" . format(username, password)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            self.tokenid = result['tokenid']
            return "username {} logged in, token {} " .format(username, self.tokenid)
        else:
            return "Error, {}" . format(result['message'])

    def showuseractive(self):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "showuseractive {} \r\n".format(self.tokenid)
        result = self.sendstring(string)
        print(string)
        if result['status'] != 'OK':
            return "Error! {}" . format(result['message'])
        else:
            return "{}" . format(json.dumps(result['messages']))

    def sendmessage(self, usernameto="xxx", message="xxx"):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "send {} {} {} \r\n" . format(
            self.tokenid, usernameto, message)
        print(string)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "message sent to {}" . format(usernameto)
        else:
            return "Error, {}" . format(result['message'])

    def inbox(self):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "inbox {} \r\n" . format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "{}" . format(json.dumps(result['messages']))
        else:
            return "Error, {}" . format(result['message'])

    def logout(self):
        if(self.tokenid == ""):
            return "Error, not authorized"
        string = "logout {} \r\n" . format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            self.tokenid = ""

if __name__ == "__main__":
    cc = ChatClient()
    while True:
        print('Aplikasi Chat')
        print('Login terlebih dahulu, dengan format: auth [username] [password]')
        print('Fitur (isi sesuai dengan format):')
        print('1. Send Message. Format: send [usernametujuan] [message]')
        print('2. Check Inbox. Format: inbox')
        print('3. Show Active User. Format: showuseractive')
        print('4. Logout. Format: logout')
        cmdline = input("Command {}:" . format(cc.tokenid))
        print(cc.proses(cmdline))

