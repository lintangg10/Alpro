#input
bil1 = int(input('masukkan  bil1: '))
bil2 = int(input('masukkan bil2: '))
bil3 = int(input('masukkan bil3: '))
bil4 = int(input('masukkan bil4: '))
bil5 = int(input('masukkan bil5: '))

#proses
terbesar = bil1
terbesar_kedua = bil2

if bil2 > terbesar:
    terbesar_kedua = terbesar
    terbesar = bil2
else:
    terbesar_kedua = bil2

if bil3 > terbesar:
    terbesar_kedua = terbesar
    terbesar = bil3
elif bil3 > terbesar_kedua:
    terbesar_kedua = bil3

if bil4 > terbesar:
    terbesar_kedua = terbesar
    terbesar = bil4
elif bil4 > terbesar_kedua:
    terbesar_kedua = bil4

if bil5 > terbesar:
    terbesar_kedua = terbesar
    terbesar = bil5
elif bil5 > terbesar_kedua:
    terbesar_kedua = bil5

# output
print("maka jawaban ", terbesar_kedua)