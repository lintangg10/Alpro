# def inisial(daftar):
#     jenis = dict()
#     for x in daftar:
#         if x[0] in jenis.keys():
#             jenis[x[0]] += 1
#             print(x, jenis[x[0]], sep='')
#         else:
#             jenis[x[0]] = 1
#             print(x)

# daftar= ("Michael","Miny","Miboli","Mautin")
# inisial(daftar)


# def hitung(dompet):
#     uang = {}
#     total_uang = 0

#     for uangg in dompet :
#         nominal = int(uangg.split()[1])
#         if nominal in uang:
#             uang[nominal] += 1
#         else :
#             uang[nominal] = 1
#         total_uang += nominal

#     for nominal, jumlah in uang.items():
#         print(f'{jumlah} lembar senilai Rp. {nominal}')
#     print(f"{total_uang}")

# dompet = ("Rp. 100000","Rp. 20000","Rp. 50000","Rp. 50000","Rp. 10000","Rp. 5000")


def hapus(data,angka): 
    data_modifikasi= list(data)
    if angka in data_modifikasi: 
        data_modifikasi.remove(angka)
        data= tuple(data_modifikasi)
        print(data)


data = ((1,2))
hapus(data,3)