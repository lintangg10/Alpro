def n_hari_kemudian(nama, n): #nama => senin, selasa,rabu,kamis,jumat,sabtu,minggu
    n = n % 7
    '''
    senin = 0
    selasa = 1
    rabu = 2
    kamis = 3
    jumat = 4
    sabtu = 5
    minggu = 6
    '''
    bobot = 0
    if nama == 'selasa':
        bobot = 1
    elif nama == 'rabu':
        bobot = 2
    elif nama == 'kamis':
        bobot = 3
    elif nama == 'jumat':
        bobot = 4
    elif nama ==  'sabtu':
        bobot = 5
    elif nama == 'minggu':
        bobot = 6
    total = (bobot + n) % 7
    if total == 0:
        print('senin')
    elif total == 1:
        print('selasa')
    elif total == 2:
        print('rabu')
    elif total == 3:
        print('kamis')
    elif total == 4:
        print('jumat')
    elif total == 5:
        print('sabtu')
    elif total == 6:
        print('minggu')        



nama = input('masukkan nama: ')
n = int(input('berapa hari kemudian: '))
n_hari_kemudian(nama, n)


#mudah
# hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
# bobot = hari.index(nama)
# bobot = (bobot+n) % 7
# print(hari[bobot])