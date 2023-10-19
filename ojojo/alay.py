'''
a, A= 4
i, I = 1
e, E = 3
s,S = 5
g, G = 9
o, O = 0
B = 8
b = 6
'''

def translate_to_alay(kalimat):
    #daftar huruf alay
    non_alay ='aAiIeEsSgGoOBb'
    alay ='44113355990086'
    #cek satu persatu karakternya
    #for i in range (len(kalimat)):=> menggunakan index
    hasil = ''
    for karakter in kalimat:
        if karakter in non_alay:
            #harus direplace
            idx = kalimat.index(karakter)
            hasil = hasil + alay[idx]
        else:
            hasil= hasil +karakter
    return hasil


#program utama
#input
kalimat = input('kalimat: ')
#proses
hasil = translate_to_alay(kalimat)
#output
print(hasil)