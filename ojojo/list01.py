def tiga_nilai_terbaik(daftar_nilai): #hasilnya tuple a,b,c
    #urutkan secara descending
    daftar_nilai.sort(reverse=True)
    hasil = tuple(daftar_nilai[:3]) #ambil tiga kedepan, konversi ke tuple
    return hasil

#program utama

#input user
n = 0
while n < 3:
    n = int(input('Masukkan n(minimal 3): '))

data = []
for i in range(n):
    nilai = int(input('Masukkan nilai: '))
    data.append(nilai)

#proses
hasil = tiga_nilai_terbaik(data)

#Output
print(f'1, {hasil[0]}\n2. {hasil[1]}\n3. {hasil[2]}')