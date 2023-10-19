'''
triple pythagoras
a**2 + b**2 = c**2
b**2 + c**2 = a**2
c**2 + a**2 = b**2
'''

def cek(a, b, c): #return True/False
    if a**2 + b**2 == c**2 :
        print(f'{a}**2 + {b}**2 = {c}**2')
        return True
    elif b**2 + c**2 == a**2:
        print(f'{b}**2 +{c}**2 = {a}**2')
    elif c**2 + a**2 == b**2:
        print(f'{c}**2 +{a}**2 = {b}**2')
    else:
        return False

#program utama
#input
a = int(input('masukkan a: '))
b = int(input('masukkan b: '))
c = int(input('masukkan c: '))

hasil = cek(a,b,c)
if hasil == True:
    print('merupakan triple pythagoras')
else: 
    print('bukan triple pythagoras')