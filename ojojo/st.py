nama1 = input('masukkan nama 1: ')
nama2 = input('masukkan nama 2: ')
nama3 = input('masukkan nama 3: ')

#hitung panjangnya
p1 = len(nama1)
p2 = len(nama2)
p3 = len(nama3)

#tentukan siapa yang terpanjang?
#jika nama1 yang terpanjang
if p1 >=p2 and p1 >=p3:
    print(nama1)
#jika nama2 yang terpanjang
elif p2 >= p1 and p2 >= p3:
    print(nama2)
#kalau tidak berarti nama3 yang paling terpanjang
else:
    print(nama3)

#tampilkan nama yang terpanjang