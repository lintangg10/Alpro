import re
from datetime import datetime, timedelta

def cari_format_tanggal(teks):
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    tanggal = re.findall(pattern, teks)
    tanggal_sekarang = datetime.now().date()
    hasil = []
    for t in tanggal:
        tanggal_dt = datetime.strptime(t, "%Y-%m-%d").date()
        selisih = (tanggal_sekarang - tanggal_dt).days
        tanggal_formatted = tanggal_dt.strftime("%Y-%m-%d")
        hasil.append(f"{tanggal_formatted} selisih {selisih} hari")
    return hasil

def proses(teks):
    pattern_tanggal = r"\d{4}-\d{2}-\d{2}"
    tanggal = re.findall(pattern_tanggal, teks)
    tanggal_skrng = datetime.now().date()
    hasil = []
    for t in tanggal:
        tanggal_dt = datetime.strptime(t, "%Y-%m-%d").date()
        selisih = (datetime.now().date() - tanggal_dt).days
        tanggal_formatted = tanggal_dt.strftime("%Y-%m-%d")
        hasil.append(f"{tanggal_formatted} selisih {selisih} hari")
    return hasil

teks = input("Masukkan Kalimat: ")
hasil_tanggal = proses(teks)

if not hasil_tanggal:
    print("Tidak ada tanggal dalam teks.")
else:
    for tanggal in hasil_tanggal:
        print(tanggal)
