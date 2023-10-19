def mengecek_anggota(y):
    anggota_pertama = y[0]
    result = True
    for anggota in y[1:]:
        if anggota != anggota_pertama :
            result = False
            break
    return result

def cek_semua_anggota(y):
    if len(y) == 0:
        result = True
    else:
        anggota_pertama = y[0]
        result = True
        for anggota in y:
            if anggota != anggota_pertama:
                result = False
                break
        print(result)      

cek1 = (90,90,90,90,90)
cek2 = (90,67,85,90,90)
cek3 = (90,85,85,85,85)
cek_semua_anggota(cek1)
cek_semua_anggota(cek2)
cek_semua_anggota(cek3)