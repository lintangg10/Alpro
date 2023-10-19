keyword = input('masukkan kata yang dicari: ')

#case sensitive = tidak peduli huruf besar /kecil
keyword = keyword.lower()

nama_file = 'data.txt'
handle = open (nama_file, 'r')
jumlah = 0
#baca dengan for in
for baris in handle:
    baris = baris.lower()
    jumlah = jumlah+baris.count(keyword)
print(f'ditemukan {jumlah} kata {keyword}')
