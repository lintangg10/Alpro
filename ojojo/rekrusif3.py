import timeit


def pangkat_rumus(x, n):
    return x**n

def pangkat_perulangan(x, n):
    hasil = 1
    for i in range(1, n+1):
        hasil = hasil * x
    return hasil

def pangkat_rekrusif(x, n):
    #base case jika 1**n, x**1, x**0
    if x == 1:
        return 1
    elif n == 1:
        return x
    elif n == 0:
        return 1
    else:
        #recursive case
        return pangkat_rekrusif(x, n-1) * x

#ambil waktu mulai
mulai = timeit.default_timer()
hasil = pangkat_rumus(11,129)
#ambil waktu selesai
selesai = timeit.default_timer()
waktu = selesai-mulai
print(f'Hasil: {hasil}')
print(f'Waktu (rumus): {waktu}')

#ambil waktu mulai
mulai = timeit.default_timer()
hasil = pangkat_perulangan(11,129)
#ambil waktu selesai
selesai = timeit.default_timer()
waktu = selesai-mulai
print(f'Hasil: {hasil}')
print(f'Waktu (perulangan): {waktu}')

#ambil waktu mulai
mulai = timeit.default_timer()
hasil = pangkat_rekrusif(11,129)
#ambil waktu selesai
selesai = timeit.default_timer()
waktu = selesai-mulai
print(f'Hasil: {hasil}')
print(f'Waktu (Rekrusif): {waktu}')


# print(pangkat_rumus(11, 129))
# print(pangkat_perulangan(11, 129))
# print(pangkat_rekrusif(11, 129))
