def parse_tanggal(tgl):
    return tgl [-2:]+ '-'+tgl[5:7] + '-' + tgl[:4]

#progtam utama
tgl = '2020-09-12'
hasil = parse_tanggal(tgl)
print(f'konversi ke DD-MM-YYYY: {hasil}')