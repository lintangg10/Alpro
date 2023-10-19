def hitung_konsonan_iteratif(string):
    konsonan = 0
    konsonan_set = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    for karakter in string:
        if karakter.isalpha() and karakter.lower() not in 'aiueo':
            konsonan += 1
    return konsonan

def hitung_konsonan_rekursif(string):
    konsonan_set = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    if len (string) == 0:
        return 0
    elif string[0].isalpha() and string[0].lower() not in 'aiueo':
        return 1 + hitung_konsonan_rekursif(string[1:])
    else:
        return hitung_konsonan_rekursif(string[1:])

string = 'Alpro'
hasil = hitung_konsonan_iteratif(string)
print(hasil)

string = 'Alpro'
hasil = hitung_konsonan_rekursif(string)
print(hasil)