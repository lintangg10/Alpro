import re

def replace_kata(kata_lama, kata_baru):
    artikel = re.sub(kata_lama, kata_baru, artikel)
    return artikel

def baca_file(nama_file):
    handle = open(nama_file)
    artikel = handle.read()
    return artikel

def update_file(nama_file, artikel):
    handle = open(nama_file, 'w')
    handle.write
    handle.close()

nama_file = input('Masukkan artikel: ')
artikel = baca_file(nama_file)

kata_lama= input('masukkan kata yang akan direplace: ')
kata_baru = input('masukkan kata penggantinya: ')

hasil = replace_kata(kata_lama, kata_baru)

update_file(nama_file, hasil)