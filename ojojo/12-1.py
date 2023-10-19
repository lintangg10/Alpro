n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}
for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi
print(data_aplikasi)

daftar_aplikasi_list = [set(aplikasi) for aplikasi in data_aplikasi.values()]

#menampilkan nama-nama aplikasi yang hanya muncul di satu kategori saja
aplikasi_satu_kategori = set()
for aplikasi_set in daftar_aplikasi_list:
    for aplikasi in aplikasi_set:
        count= sum(aplikasi in aplikasi_set for aplikasi_set in daftar_aplikasi_list)
        if count ==1:
            aplikasi_satu_kategori.add(aplikasi)

print("Aplikasi yang hanya muncul di satu kategori saja:")
print(aplikasi_satu_kategori)

#menampilkan nama-nama aplikasi yang muncul tepat di dua kategori sekaligus
aplikasi_dua_kategori = set()
for aplikasi_set in daftar_aplikasi_list:
    for aplikasi in aplikasi_set:
        count = sum(aplikasi in aplikasi_set for aplikasi_set in daftar_aplikasi_list) 
        if count ==2:
            aplikasi_dua_kategori.add(aplikasi)

print("Aplikasi yang muncul tepat di dua kategori sekaligus:")
print(aplikasi_dua_kategori)
