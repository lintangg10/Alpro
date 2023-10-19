def data_diri():
    data = []
    nama = input('Nama: ')
    nim  = input('NIM: ')
    alamat = input('Alamat: ')

    data.append(nama)
    data.append(nim)
    data.append(alamat)

    result = data

def proses_data_diri(biodata):
    nama = biodata [0]
    nim = biodata[1]
    alamat = biodata[2]

    print('Nama: '+nama)
    print('NIM: '+nim)
    print('Alamat: '+alamat)

    nimm = tuple(nim)
    namaa_depaan = tuple(nama.split()[0].lower())
    namaa_dibalikk = tuple(nama.split()[::-1])
    
    
    print('NIM: '+str(nimm))
    print('Nama Depan: '+str(namaa_depaan))
    print('Nama Terbalik: '+ str(namaa_dibalikk))

dataa1 =('Debora Lintang Kusumaningrum', '71220952', 'Purworejo', 'Jawa Tengah')
proses_data_diri(dataa1)