#inut
suhu = float(input('masukkan suhu: '))

#demam atau tidak? demam jika >= 38
if suhu <34.0:
    print('mati kedinginan')
elif 34.0 <= suhu <= 37.0:
    print('suhu tubuh normal')
elif 37.1<=suhu <=40.0:
    print('demam')
else: 
    print('Mati kepanasan')

    '''
    coba untuk tambahkan kemungkinan
    <34 = mati kedingnan
    34-37 = aman
    38-39 = demam
    >40 = mati kepanasan
    '''