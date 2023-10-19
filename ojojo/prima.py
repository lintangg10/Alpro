import math

def is_prime(number):
    pembagi = 0
    for i in range(1,(number+1)):
        if number % i == 0:
            pembagi +=1 #pembagi = pembagi +1
    if pembagi ==2:
        return True
    else:
        return False

#program utama
# number = int(input('masukkan bilangan: '))
# hasil = is_prime(number)
# if hasil:
#     print('Bilangan Prima')
# else:
#     print('Bukan Prima')

#program utama
bawah = int(input('batas bawah: '))
atas = int(input('batas atas: '))

for i in range(bawah, atas+1):
    hasil = is_prime(i)
    if hasil:
        print(i)
