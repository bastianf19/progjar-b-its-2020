# Repository Pemrograman Jaringan B
## Tugas 1 :
- Jalankan program server.py di 3 port yang berbeda (31000, 31001, 31002) 
- Jalankan program client.py untuk konek ke server yang jalan pada poin sebelumnya dan mengirimkan string “PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA”
- Jalankan program server.py di 3 port yang berbeda di 2 komputer yang berbeda 
- Jalankan program client.py untuk konek ke server pada poin sebelumnya, kirimkan string yang sama
- Jalankan program server.py di 2 komputer yang berbeda, masing-masing 2 server di port yang berbeda 
- MODIFIKASILAH program client.py dan server.py agar dapat MENTRANSFER file dari client ke server (letakkan program modifikasi di direktori tugas1a) 
- MODIFIKASILAH program server.py agar dapat mengirimkan MENTRANSFER FILE yang di request oleh client (letakkan program modifikasi di direktori tugas1b) 
- LETAKKAN di repository github anda SENDIRI dengan folder tugas1 
### Hasil Tugas1 terdapat di dalam folder /tugas1/Hasil
- File hasil_tugas1-1.jpg berisi server1.py dan server2.py yang sedang dijalankan. Ketika client melakukan koneksi berdasarkan port kedua server tersebut, maka terjadi koneksi di masing-masing server.
- File hasil_tugas1-2.jpg berisi server3.py dan client.py yang sedang dijalankan. Ketika client melakukan koneksi ke server3, maka akan terjadi koneksi. Client dijalankan sebanyak 3 kali, yaitu melakukan koneksi ke server1.py, server2.py, dan server3.py
- File hasil_tugas1a.jpg berisi server.py dan client.py yang sedang dijalankan. Ketika dijalankan, maka client.py membaca file.txt, kemudian isi dari file tersebut dikirimkan ke server. Pada server file dibaca, ditampilkan pada konsole, dan ditulis kedalam file hasil.txt.
- File hasil_tugas1b-1.jpg berisi server.py dan client.py yang sedang dijalankan. Ketika dijalankan, maka dari client user menginput nama file, kemudian nama file tersebut diberikan ke server. Pada server, server mencari dan membaca isi file sesuai nama file yang diberikan, kemudian isi file tersebut diberikan kembali ke client. Pada client isi file kemudian disimpan kedalam sebuah file. File yang diproses adalah file bertipe txt.
- File hasil_tugas1b-2.jpg berisi server.py dan client.py yang sedang dijalankan. Ketika dijalankan, maka dari client user menginput nama file, kemudian nama file tersebut diberikan ke server. Pada server, server mencari dan membaca isi file sesuai nama file yang diberikan, kemudian isi file tersebut diberikan kembali ke client. Pada client isi file kemudian disimpan kedalam sebuah file. File yang diproses adalah file bertipe image.
## Tugas 2:
- Menangkap paket menggunakan wireshark pada udp_simpel.py pada jaringan lokal (127.0.0.1, port 5005).
- Menangkap paket menggunakan wireshark pada udp_fileclient.py pada jaringan lokal (127.0.0.1, port 5005).
- Menangkap paket menggunakan wireshark pada udp_simpel.py pada komputer lain melalui wifi (192.168.1.13, port 5005 pada komputer teman saya).
- Menangkap paket menggunakan wireshark pada udp_fileclient.py pada komputer lain melalui wifi (192.168.1.13, port 5005 pada komputer teman saya).

## Tugas 3:
Menambahkan Threading agar program dapat mendownload file bersamaan.

## Tugas 4:
### Rancanglah sebuah protokol untuk: 
- Meletakkan file
- Mengambil file
- Melihat list file
### Buatlah dokumentasi dari protokol tersebut berisikan:
- Ketentuan membaca format
- Daftar fitur
- Cara melakukan request
- Apa respon yang didapat
### Gunakan format JSON untuk tugas ini
### Buatlah client untuk setiap operasi tersebut

## Tugas 5:

- Jalankan program server diatas, cobalah chat-cli untuk berkomunikasi dengan server
- Buatlah dokumentasi protokol untuk layanan chat diatas. Dokumentasi mempunyai format yang akan dijelaskan di nomor 3b
- Berdasarkan program diatas, tambahkan fitur
  - Untuk memperlihatkan pengguna pengguna lain yang lain
  - Melogout user yang sedang aktif
- Format dokumentasi :
Buatlah dokumen di msword online, kirimkan link dokumen tersebut di ms teams
Format :
```
NAMA SERVICE :
DESKRIPSI:
<contoh> service ini merupakan ...

FORMAT DATA:
<contoh>
Komunikasi dikirimkan ke socket dengan mengirimkan teks alfanumerik dengan format
COMMAND spasi PARAMETER1 spasi PARAMETER2 dst...

DAFTAR FITUR:
Nama fitur:
Deskripsi dan tujuan
Parameter input
Hasil keluaran, penjelasan status keluaran 
Contoh message input dan keluaran
Nama Fitur 2 … dst
```
## Tugas 6
Buatlah
- Sebuah multithreaded server, buka pada port 10001 di ip address 127.0.0.1
- Dapat melayani request dalam bentuk string seperti ini
`GET spasi / spasi HTTP/1.0` 
- Tanda akhir request adalah `“\r\n\r\n”`
- Jika tanda akhir request diterima, maka balaslah dengan string 
`“<h1>SERVER HTTP</h1>”`
- Cobalah dengan telnet pada port 10001, dengan cara mengirimkan string 
`GET<spasi>/<spasi>HTTP/1.0<enter><enter>`
- Harusnya mereply dengan yang sama pada point nomor 4
- Bukalah chrome web browser, aktifkan developer mode, bagian network
- bukalah alamat `http://127.0.0.1:10001`
- Screenshot-lah tampilannya
- Kirimkan ke asisten

## Tugas 7

### Performance test sederhana, hanya bisa dilakukan di linux/unix based
- Gunakan apachebenchark , dengan command ab
- Testlah server anda dengan :
`ab -n <jumlahrequest> -c <concurency> http://127.0.0.1:10001/`
- Concurrency melambangkan user yang mengakses secara bersamaan, concurency berbeda dengan paralel, concurency adalah bagaimana satu resource dibagi ke sekian banyak request yang meminta layanan

## Tugas 8
- Updatelah kembali repository rm77
- Buka folder progjar5
- Dalam file http.py, telah ada implementasi method post yang masih kosong
- Jalankan server pada `ip 127.0.0.1 dengan port 10002`
- Bukalah browser arahkan ke`http://127.0.0.1:10002/sending.html`, isilah dengan sesuatu dan kirim
  - Keterangan: sending.html merupakan file dengan format HTML yang dapat digunakan untuk mengambil input dari client dan mengirimkannya ke server
- Akan keluar tulisan ‘kosong’
- Modifikasilah agar server dapat membalas dengan isi
  - semua  header yang dikirim dari browser
  - Yang anda isikan di form pada saat mengisi pada poin nomor 5, misalkan mengisi “ISILAH” maka server akan mereply dengan “ISILAH” juga , dan bukan ‘kosong’
- Laporkan aktifitas anda kepada asisten