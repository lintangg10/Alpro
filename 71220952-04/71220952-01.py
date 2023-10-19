'''
januari, maret, mei, juli, agustus, oktober, desember = 31
februari = 28
april, juni, september, november = 30
'''
def jumlah_hari(nama_bulan):
    if nama_bulan == 'januari' or nama_bulan =='maret' or nama_bulan == 'mei' or nama_bulan == 'juli' or nama_bulan == 'agustus' or nama_bulan== 'oktober' or nama_bulan == 'desember':
        print('output: 31')
    elif nama_bulan == 'april' or nama_bulan == 'juni' or nama_bulan == 'september' or nama_bulan == 'november':
        print('output: 30')
    elif nama_bulan == 'februari':
        print ('output: 28')
    else:
        print('Tidak Valid')



