cigars = int(input('masukkan jumalah rokok: '))
weekend = input('Apakah weekend? (Y/N): ')
is_weekend = False

if weekend == 'Y'or weekend == 'y':
    is_weekend = True

if is_weekend == True and cigars >= 40:
    print ('sukses') 
elif is_weekend == False and 40<= cigars <= 60:
    print('sukses')
else:
    print ('gagal')
