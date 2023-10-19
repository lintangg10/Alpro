def hari_kemudian(nama, n):
    # List nama-nama hari
    hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
    # Mencari bobot hari yang diinputkan
    bobot = hari.index(nama)
    # Menentukan nama hari n hari kemudian
    bobot = (bobot + n) % 7
    return hari[bobot]

# Input dari user
nama = input("Masukkan nama hari: ")
n = int(input("Masukkan jumlah hari: "))

# Percabangan untuk memastikan input yang valid
if nama in ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu'] and n >= 0:
    # Menampilkan nama hari n hari kemudian
    print("Hari {} hari ke-{} adalah {}".format(nama, n, hari_kemudian(nama, n)))
else:
    print("Input tidak valid.")


