# Repository Pemrograman Jaringan B
## Tugas1 :
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
