def selisih_hari(tanggal1, bulan1, tanggal2, bulan2):
    hari_bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    if bulan1 == '1' or bulan1 =='3' or bulan1 == '5' or bulan1 == '7' or bulan1 == '8' or bulan1 == '10' or bulan1 == '12':
        selisih_1 = (31-tanggal1) + tanggal2
        print(selisih_1)
    elif bulan1 == '4' or bulan1 == '6' or bulan1 == '9' or bulan1 == '11':
        selisih_2 = (30-tanggal1) + tanggal2
        print(selisih_2)
    elif bulan1 == '2':
        selisih_3: (28-tanggal1) + tanggal2
        print(selisih_3)


