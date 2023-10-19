#input
bil1 = int(input('masukkan bil1 (10-99): '))
bil2 = int(input('masukkan bil2(10-99): '))

#proses
puluhan_1 = bil1 // 10
satuan_1 = bil1 % 10
puluhan_2 = bil2 // 10
satuan_2 = bil2 % 10

if puluhan_1 == puluhan_2 or puluhan_1 == satuan_2 or puluhan_2 == satuan_1 or satuan_1 == satuan_2:
    print('sama')
else:
    print('tidak sama')
