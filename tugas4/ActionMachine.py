from ActionHandler import Action
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

Menambahkan/Meletakkan File
Digunakan untuk menambahkan file ke dalam folder file
  Request : add
  Parameter : [namafile] [isi_filenya]
  Response : berhasil -> File Ditambahkan
             gagal -> error

Mengambil File
Digunakan untuk mengambil file berdasarkan namafile dari folder file
  request: get
  parameter : [namafile] yang akan diambil
  response: File berhasil di download pada tempat client dijalankan

Melihat List File
Digunakan untuk mengambil list file dari folder file
  request: list 
  parameter: -
  response: Mendapatkan list file yang terdapat pada folder file

Jika command tidak dikenali akan merespon dengan ERRCMD
'''
p = Action()

class MAction:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='add'):
                print('command : add')
                namafile = cstring[1].strip()
                file = cstring[2].strip()
                # print(namafile, file.encode())
                p.add_file(namafile, file.encode())
                return ("Done")

            elif (command == 'get'):
                print('command : get')
                namafile = cstring[1].strip()
                # print(namafile)
                hasilnya = p.get_data(namafile)
                return (hasilnya)

            elif (command=='list'):
                dt = {}
                dt['namafile'] = []
                hasilnya = p.list_data()
                for namafile in hasilnya:
                    dt['namafile'].append({'namafile':namafile})
                return json.dumps(dt, indent=4)
            
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    ma = MAction()
