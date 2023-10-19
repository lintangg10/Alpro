kata = input('Kata yang dicari: ')

kata = kata.lower()

nama_file1 = 'romeojuliet.txt'
handle = open (nama_file1, 'r')
jumlah = 0

for baris in handle:
    baris = baris.lower()
    jumlah = jumlah+baris.count(kata)
print(f'Kata {kata} jumlahnya ada: {jumlah}')