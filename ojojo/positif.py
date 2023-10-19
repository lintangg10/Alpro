#input
bilangan = int(input('masukkan sebuah bilangan: '))

#jika positif
if bilangan > 0:
    print('positif')
#negatif
elif bilangan < 0:
    print('negatif')
else: #bisa juga -> elif bilangan ==0:
    print('nol')