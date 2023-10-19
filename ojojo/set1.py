data = [1,3,4,5,2,3,2,4,5,5,4,1,3,7]
data_unik = set()

#masukkan dalam data unik dalam posisi tidak ada yang sama
#cara 1 = perualangan biasa

hasil = []
for nilai in data:
    if nilai not in hasil:
        hasil.append(nilai)
print(hasil)

#cara 2 : pakai set
hasil = set()
for nilai in data:
    hasil.add(nilai)
print(list(hasil))