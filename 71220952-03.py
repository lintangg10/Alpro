nama_file = 'nilai.txt'
handle = open(nama_file, 'r+')

isi_file = open('nilai.txt', 'r')
awal_nilai = [int(line.strip()) for line in isi_file]
isi_file.close()

#pake list untuk menentukan tempat
nilai_akhir = awal_nilai[0]*0.05 + awal_nilai[1]*0.05 + awal_nilai[2]*0.1 + awal_nilai[3]*0.05 + awal_nilai[4]*0.15 + awal_nilai[5]*0.1 + awal_nilai[6]*0.22 + awal_nilai[7]*0.28

print("Nilai Tugas 1:", awal_nilai[0])
print("Nilai Tugas 2:", awal_nilai[1])
print("Nilai Tugas 3:", awal_nilai[2])
print("Nilai Tugas 4:", awal_nilai[3])
print("Nilai Tugas 5:", awal_nilai[4])
print("Nilai Tugas 6:", awal_nilai[5])
print("Nilai Ujian Tengah Semester:", awal_nilai[6])
print("Nilai Ujian Akhir Semester:", awal_nilai[7])

print("Nilai akhir: %.2f" % nilai_akhir)





