nama_file = 'D:\\Semester 2\\Laprak PraAlPro\\ojojo\\data.txt'
#windows
#nama_file = 'D:\\Android\\data.txt'

handle = open (nama_file, 'r') #read only
# mode = r,w,a,b
#baca semua
#1. handle.readlines() -> list
#2. handle.read() -> string
#3. handle.readline()-> string, 1 baris di posisi sekarang
hasil = handle.readlines()
print (hasil)
print (f'ada {len(hasil)} baris')

# n = 3
# no_baris = 1

# for baris in handle:
    # if no_baris == n:
    #     #hanya menampilkan baris ke-n saja 
    #     print(baris, end="")
    # no_baris = no_baris + 1 

#harus selalu ditampilkan
# handle.close()