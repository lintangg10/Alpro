#input
ja = int(input('Jam awal= '))
ma = int(input('Menit awal= '))

jah = int(input('Jam akhir: '))
mw = int(input('Menit awal: '))

#hitung selisih dalam menit
jam = 60

ht = abs(ja - jah)
htng = ma - mw

total = (ht * jam) - htng

print('Selisihnya adalah',total, 'menit' )