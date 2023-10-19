data = [ #list of tuples
    (100, 'Bambang', 3.76), 
    (98, 'Wati', 2.12), 
    (102,'Agus', 1.23), 
    (101, 'Bejo', 0.86)
 ]

#tampilkan jumlah orang
print(f'ada {len(data)} orang')

#tampilkan dengan urutan nomor
data.sort() #default ascending, pakai key index ke-0
print(data)

#tampilkan dengan urutan nama
data.sort(key=lambda x: x[1]) #ascending, pakai key index ke-1
print(data)

#urutkan berdasarkan ipk terbaik
data.sort(key=lambda x: x[2], reverse=True) #ascending, pakai key index ke-2
print(data)

#tampilkan data lengkap orang bernama wati
print(data)

#berapa ipknya Wati
print(data[1],[2])

#tambah data Joni, no.99 dengan IPK 4.0
data.append((99, 'Joni', 4.0))

#urutkan berdasarkan ipk
data.sort(key=lambda x:x[2]) #ascending berdasarkan ipk
print(data)

#ubah ipknya agus menjadi 3.0
agus = (102, 'Agus', 3.0)
#hapus agus dari list
del data[0]
#masukkan agus ke dalam list
data.append(agus)


#urutkan berdasarkan ipk
data.sort(key=lambda x:x[2]) #ascending berdasarkan ipk
print(data)
