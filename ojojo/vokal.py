def hitung_vokal(kalimat):
    #siapkan daftar huruf vokal, huruf besar dan kecil
    vokal = 'aAiIuUeEoO'
    jumlah = 0
    #cek satu persatu karakter
    for karakter in kalimat:
        #jika karakter di dalam huruf vokal
        if karakter in vokal:
            jumlah+=1
    return jumlah

def hitung_konsonan(kalimat):
    vokal = 'aAiIuUeEoO'
    jumlah = 0
    for karakter in kalimat:
        #bukan vokal tapi masuk alphabet
        if karakter not in vokal and karakter.isalpha():
            jumlah+=1
    return jumlah

def hitung_digit(kalimat):
    digit= '0123456789'
    jumlah = 0
    for karakter in kalimat:
        if karakter in digit:
            jumlah += 1
    return jumlah


def hitung_whitespace(kalimat):
    jumlah = 0
    for karakter in kalimat:
        if karakter.isspace():
            jumlah=jumlah+1
    return jumlah

#program utama
#input
kalimat = input('kalimat: ')
#proses
hasil = hitung_vokal(kalimat)
hasil2 = hitung_konsonan(kalimat)
hasil3 = hitung_digit(kalimat)
hasil4 = hitung_whitespace(kalimat)
#output
print(f'jumlah huruf vokal: {hasil}')
print(f'jumlah huruf konsonan: {hasil2}')
print(f'jumlah digit: {hasil3}')
print(f'jumlah white space: {hasil4}')