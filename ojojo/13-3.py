def cari_huruf_besar_pertama_rekursif(string):
    if len (string) == 0 or not any (karakter.isupper() for karakter in string) :
        return None
    elif string[0].isupper():
        return string[0]
    else:
        return cari_huruf_besar_pertama_rekursif(string[1:])

string = 'Algoritma dan Pemograman'
huruf_besar_pertama = cari_huruf_besar_pertama_rekursif(string)
print(huruf_besar_pertama)