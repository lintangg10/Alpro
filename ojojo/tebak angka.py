import random

def generate_angka(bawah, atas):
    angka_komputer =  random.randrange(bawah, atas)
    return angka_komputer

#program utama
#input level
langkah = 6
angka_komputer = 0
level = int(input('masukkan level 1/2/3: '))
if level == 1: #easy
   print('level easy')
   angka_komputer = generate_angka(0, 10)
   langkah = 6
elif level == 2: #intermediete
    print('level intermediate')
    angka_komputer = generate_angka(0,1000)
    langkah = 10
else: #hard
    print('level hard')
    angka_komputer = generate_angka(0,1_000_000)
    langkah = 12



tebakan = False

hasil = False #kalah
while tebakan ==  False: #selama tebakan masih false, ulangi terus
    if langkah == 0:
        break
    tebakan_user = int(input('masukkan tebakan anda: '))
    langkah = langkah - 1
    if tebakan_user == angka_komputer:
        tebakan = True
        hasil = True
        break
    else:
        if tebakan_user > angka_komputer:
            print('terlalu besar')
        else:
            print('tebakan anda terlalu kecil')
        print('Tebakan anda masih salah! silahkan ulangi lagi...')
if hasil == True :
    print(f'selamat Anda menang. Tebakan anda benar. Sisa: {langkah}')
else:
    print('Anda Kalah, sudah kehabisan langkah')