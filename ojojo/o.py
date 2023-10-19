#input dalam rupiah
rupiah = int(input('masukkan dalam rupiah: '))

#hitung kursnya
usd = int(rupiah / 14500)
yen = rupiah / 130
sin = rupiah / 10400
eur = rupiah / 16200

#output dalam $USD, yen, $Sin, Euro
print(f'Rp {rupiah} setara dengan: ')
print(f'{usd} US$')
print(f'{yen} yen')
print(f'{sin} sin$')
print(f'{eur} Euro')


'''
kurs 
1 USD = Rp. 14500
1 Yen = Rp. 130
1 Sin = Rp. 10400
1 Euro = Rp. 16200
'''
