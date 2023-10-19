#input
upah_per_jam = 10000
jam_per_hari = 8

#proses
hari_kerja = int(input('n = '))
upah_bruto = upah_per_jam * jam_per_hari * hari_kerja
pajak = upah_bruto * 0.05
upah_netto = upah_bruto - pajak

#output
print("Upah karyawan sebelum pajak: Rp.", upah_bruto)
print("Pajak yang harus dibayar: Rp.", pajak)
print("Penghasilan bersih yang diterima: Rp.", upah_netto)