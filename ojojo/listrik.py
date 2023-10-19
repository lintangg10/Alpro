def tagihan_listrik(pemakaian, golongan=3):
    bayar = 0
    pemakaian_100 = 100 if pemakaian > 100 else pemakaian
    pemakaian_100_lebih = pemakaian - pemakaian_100
    if golongan == 1:
        bayar = pemakaian_100 * 1500 + pemakaian_100_lebih * 2000
    elif golongan == 2:
         bayar = pemakaian_100 * 2500 + pemakaian_100_lebih * 3000
    elif golongan == 3:
         bayar = pemakaian_100 * 4000 + pemakaian_100_lebih * 5000
    elif golongan == 4:
          bayar = pemakaian_100 * 5000 + pemakaian_100_lebih * 7000
    return bayar

print(tagihan_listrik(130))
print(tagihan_listrik(80, 4))
print(tagihan_listrik(golongan=1, pemakaian=175))