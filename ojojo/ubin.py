#input jumlah 1 meter, 5 meter dan panjang
ubin1 = int(input('masukkan jumlah ubin 1 meter: '))
ubin5 = int(input('masukkan jumlah ubin 5 meter: '))
panjang = int(input('masukkan panjang yang ingin ditutupi ubin: '))

#cek dulu panjang totalnya bisa apa enggak?
if (1 * ubin1 + 5 * ubin5 ) >= panjang:
    #berarti mungkin bisa
    #cek apakah cukup pakai ubin5
    if panjang % 5 == 0 and panjang//5<=ubin5:
        print('bisa')
    elif panjang % 5 <= ubin1:
        print ('bisa')
    else: 
        print('tidak bisa')
else:
    #tidak bisa karna tidak cukup
    print('Tidak bisa')