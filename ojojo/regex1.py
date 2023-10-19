import re

def baca_file(nama_file):
    handle = open(nama_file)
    artikel = handle.read()
    return artikel

def proses_regex(artikel):
    # pattern = '[A-Z][a-z]*'
    # pattern = 'Jakarta'
    pattern = '\w{5}'
    #coba dengan fungsi search=> yang pertama ketemu
    #hasil = re.search(pattern, artikel)

    #pakai findall => ketemu semua, dalam bentuk list
    hasil = re.findall(pattern, artikel)
    print(f'Ditemukan{len(hasil)} kata Jakarta')
    return hasil

#program utama
#minta input
nama_file = input('Masukkan artikel: ')
#proses
artikel = baca_file(nama_file)
hasil = proses_regex(artikel)
#output
print(hasil)