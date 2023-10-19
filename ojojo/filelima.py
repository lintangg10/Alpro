#baca isinya dulu
nama_file = 'data.txt'
handle = open (nama_file, 'r')
isi_file = handle.read()
print(f'isi file sekarang: ')
print(isi_file)
handle.close()

#setiap nambah baris, perlu enter apa ga
perlu_enter = True
#ngecek apakah kaarakter terakhir perlu enter
if isi_file[-1]=='\n':
    perlu_enter = False

#tambahkan satu baris di belakang
tambahan = input('masukkan tambahan baris: ')
if perlu_enter:
    tambahan = '\n' + tambahan

#simpan
handle = open(nama_file, 'a')
handle.write(tambahan)
handle.close()
