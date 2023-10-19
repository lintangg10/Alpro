# # def hitungHonorAsisten(data, besaranHonor):
# #     result = {}

# #     for matkul in data:
# #         for asdos in data[matkul]:
# #             if asdos not in result:
# #                 result[asdos] = besaranHonor
# #             else:
# #                 result[asdos] += besaranHonor

# #     result = {k: v for k, v in sorted(result.items(), key=lambda item: item[0])}
# #     return result

# # data = {
# #     'Alpro_A':['Rizky', 'Yusak', 'Shalom', 'Tania'],
# #     'Alpro_B':['Dedi', 'Karen', 'Yusak', 'Tania'],
# #     'Alpro_C':['Richard', 'Rizky', 'Mikael', 'Yusak'],
# #     'Alpro_D':['Michelle', 'Tania','Dedi','Karen'],
# #     'Jarkom_A':['Rizky', 'Vero'],
# #     'Jarkom_B':['Riel','Natanael'],
# #     'Jarkom_C':['Yulius','Kevin']
# # }
# # print(hitungHonorAsisten(data,45000))

# # def kata_unik_spesial(kalimat1, kalimat2):
# #     kalimat = kalimat1 + " " + kalimat2
# #     kata_list = kalimat.lower().split()
# #     kata_count = {}
# #     for kata in kata_list:
# #         kata_count[kata] = kata_count.get(kata, 0) + 1

# #     kata_unik_spesial = set()
# #     for kata, count in kata_count.items():
# #         if count <= 2:
# #             kata_merged = kata*count
# #             kata_unik_spesial.add(kata_merged)

# #     return kata_unik_spesial


# # hasil = kata_unik_spesial('saya mau makan', 'saya mau mandi')
# # print(len(hasil))
# # print(sorted(hasil))

# # def daftar_tidak_sama(angka1, angka2, batas):
# #     himpunan1 = set(range(angka1, batas, angka1))
# #     himpunan2 = set(range(angka2, batas, angka2))

# #     jumlah_tidak_sama = len(himpunan1.symmetric_difference(himpunan2))
# #     print(jumlah_tidak_sama)

# # daftar_tidak_sama(7, 3, 30)

# def cek_kekurangan(krs1, krs2):
#     lower_krs1 = [matakuliah.lower() for matakuliah in krs1]
#     lower_krs2 = [matakuliah.lower() for matakuliah in krs2]
#     count = 0
#     for matakuliah in lower_krs1:
#         if matakuliah not in lower_krs2:
#             count += 1
#     print(count)

# krs1 = ['alpro', 'strukdat', 'pbo', 'ppkn', 'toefl', 'prakalpro', 'skripsi', 'kkn', 'statistik', 'ai', 'jarkom', 'tekwan']
# krs2 = ['alpro', 'jarkom', 'pbo', 'strukdat', 'statistik', 'hamdem', 'kcp']
# cek_kekurangan(krs1, krs2)