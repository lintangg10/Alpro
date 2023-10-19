def cek_palindrome(kalimat):
    #palindrome hanya mengecek alfabet (A-Z dan a-z)
    #konversi semuanya ke huruf kecil
    kalimat = kalimat.lower()
    #buang semua yang bukan alphabet
    for karakter in kalimat:
        if karakter.isalpha():
            hasil = hasil +karakter

    balik = kalimat[::-1]
    if kalimat == balik:
        print('Palindrome!')
    else:
        print('Bukan Palindrome!')

kalimat = input('kalimat: ')
cek_palindrome(kalimat)