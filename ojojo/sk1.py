def fibo(batas):
    bil1 = 1
    bil2 = 1
    # tampilkan dua suku fibonacci pertama
    if bil1 < batas:
        print(bil1, end='\t')
        print(bil2, end='\t')
    # suku-suku berikutnya dari bil1 + bil2
    suku_baru = bil1 + bil2
    while suku_baru < batas:
        print(suku_baru, end='\t')
        # geser bil1 dan bil2
        bil1 = bil2
        bil2 = suku_baru
        # hitung lagi suku berikutnya
        suku_baru = bil1 + bil2

# program utama
batas = int(input('Masukkan batas dari deret fibonacci: '))
fibo(batas)