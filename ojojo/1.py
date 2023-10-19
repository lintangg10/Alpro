#input 
masukan = int(input ('masukkan angka positif (1000 - 9999):'))

#proses 
depan = masukan // 1000
belakang = masukan % 10
total = depan + belakang 

#output
print(f'total: {total}')


#set
#input 
masukan = int(input ('masukkan angka positif (1000 - 9999):'))
#proses
total = int(masukan[0]) + int(masukan[-1])
 #output
print(f'total: {total}')