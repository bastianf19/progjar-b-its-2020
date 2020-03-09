import logging
import requests
import os
import threading


def download_gambar(url=None, name=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png'] = 'png'
    tipe['image/jpg'] = 'jpg'
    tipe['image/jpeg'] = 'jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = '/tugas3/foto/' + name
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}", "wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__ == '__main__':
    ln = []
    ln.append('https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg')
    ln.append(
        'https://www.its.ac.id/wp-content/uploads/2020/01/Sosial-Media-NDSC_LinkedIn-1-1024x535.jpg')
    ln.append(
        'https://www.its.ac.id/wp-content/uploads/2020/01/Sosial-Media-NDSC_LinkedIn-2-1024x535.jpg')
    ln.append(
        'https://www.its.ac.id/wp-content/uploads/2020/01/Sosial-Media-NDSC_LinkedIn-3versi1-1024x535.jpg')
    ln.append(
        'https://www.its.ac.id/wp-content/uploads/2020/02/duta-kampus-01-1.jpg')
    threads = []
    for i in range(0, len(ln)):
        dw_thread = threading.Thread(
            target=download_gambar, args=(ln[i], 'foto ke '+str(i)))
        threads.append(dw_thread)
    for thread in threads:
        thread.start()
