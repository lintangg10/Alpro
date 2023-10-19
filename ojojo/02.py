#input
masukan = input ('masukkan angka positif (maks 9999):')

#proses 
# ribuan = masukan // 1000
# ratusan = masukan // 100 - ribuan * 10
# puluhan = masukan // 10 - ratusan * 10 - ribuan *100
# satuan = masukan % 10

total = 0
for number in masukan: 
    total = total + int(number)


#ouput
print(f'hasil penjumlahan semua digit adalah: {total}')
