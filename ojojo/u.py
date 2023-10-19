def tukar (a, b):
    temp = b
    b = a
    a = temp
    return a,b #tuple


a = int(input('nilai a: '))
b = int(input('nilai b: '))
print(f'sebelum ditukar, a: {a}, b: {b}')
a, b = tukar(a, b)
print(f'setelah ditukar, a: {a}, b: {b}')

