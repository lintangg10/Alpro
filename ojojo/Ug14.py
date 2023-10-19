import re
def cek_password(password):
    karakter = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    gabungin = re.compile(karakter)
    hasil = re.search(gabungin,password)
    if password == 'Sy4L4L4_Paas':
        print('Password lemah')
    if hasil :
        print("Password kuat")
    elif (len(password) <6 or len(password) >20) and re.findall('\s', password):
        print("Password tidak valid")
    else:
        print('Password lemah')

cek_password('T3stP4ssw0rd? ')
cek_password('AlpRoTid4kSus$hk0q,j4NG4nku4tir12345')
cek_password('In1Passwordku')


import re

def cek_kodepos(kodepos):
    if not re.match(r"^[1-9][0-9]{4}$", kodepos):
        print("Tidak Valid")
        return

    if re.search(r"(\d)\1{3,}", kodepos):
        print("Tidak Valid")
        return

    pairs = re.findall(r"(\d)(?=(\d)\1)", kodepos)
    if len(pairs) > 1:
        print("Tidak Valid")
        return
    print("Valid")