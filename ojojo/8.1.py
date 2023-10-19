nama_file = 'bunglon.txt'
handle = open (nama_file, 'r')
isi_file1 = handle.readlines()

nama_file = 'cicak.txt'
handle = open (nama_file, 'r')
isi_file2 = handle.readlines()

for i in range (len(isi_file1)) :
    if isi_file1[i] != isi_file2[i]:
        print("Perbedaan pada baris", i+1)
        print("File 1:", isi_file1[i])
        print("File 2:", isi_file2[i])
