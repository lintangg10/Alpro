word_set = set()
#membaca file pertama
fname1 = input("Masukkan Nama File Pertama: ")
try:
    fhand1 = open(fname1)
except FileNotFoundError:
    print("File Tidak Bisa Dibuka:", fname1)
    exit()
for line in fhand1:
    words = line.lower().split()
    for word in words:
        word_set.add(word)
fhand1.close()

# membaca file kedua
fname2 = input("Masukkan Nama File Kedua: ")
try:
    fhand2 = open(fname2)
except FileNotFoundError:
    print("File Tidak Bisa Dibuka:", fname2)
    exit()
for line in fhand2:
    words = line.lower().split()
    for word in words:
        word_set.add(word)
fhand2.close()

# menampilkan semua kata yang muncul pada kedua file
print("Kata-kata yang muncul pada kedua file:")
sorted_word = sorted(word_set, key=lambda X: X[0])
for word in sorted_word:
    print(word)
