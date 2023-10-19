nama_file = 'buah.txt'
handle = open(nama_file, 'r+')
nama_buah = handle.read()
nama_buah = nama_buah.lower()
handle.close()

nama_buah_dihapus = input('Masukkan kata yang ingin dihapus: ')
nama_buah_dihapus = nama_buah_dihapus.lower()

if nama_buah.count(nama_buah_dihapus) == 0:
    print(f'Kata {nama_buah_dihapus} tidak ada di dalam file!')
else:
    handle = open(nama_file, 'w')
    for line in nama_buah.split('\n') :
        if line.strip().lower() == nama_buah_dihapus:
            continue 
        handle.write(line + '\n')
    handle.close()
    print(f'Kata {nama_buah_dihapus} telah dihapus dari file.')


