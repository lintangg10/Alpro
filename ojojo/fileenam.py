#baca semua isi filenya dalam bentuk stirng
nama_file = 'data.txt'
handle = open (nama_file, 'r+')
isi_file = handle.read()
isi_file = isi_file.lower()
handle.close()

#input user
kata_asli = input('masukkan kata yg diganti: ')
kata_asli = kata_asli.lower()

#cari apakah kata yang mau diganti ada?
if isi_file.count(kata_asli)==0:
    #tidak ada..batal
    print(f'Kata {kata_asli} tidak ada di dalam file!')
else:
    #kalau ada, lakukan penggantian dengan metode replace
    kata_ganti = input('kata ganti: ')
    kata_ganti = kata_ganti.lower()
    handle = open (nama_file, 'w')
    isi_file = isi_file.replace(kata_asli, kata_ganti)
    #tulis ke replace
    handle.write(isi_file)
    handle.close()
