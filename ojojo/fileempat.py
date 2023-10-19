# nama_file = 'data.txt'
nama_file = 'belum.txt'
handle = open (nama_file, 'w') #write

isi_file = input('masukkan isi file: ')
handle.write(isi_file) #overwrite
handle.close()