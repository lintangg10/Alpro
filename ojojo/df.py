def kata_terpendek_terpanjang(kalimat): 
    kata_terpendek = None
    kata_terpanjang = None
    # Memisahkan kalimat menjadi kata-kata
    kata_kalimat = kalimat.split()
    # Mencari kata terpendek dan terpanjang
    for kata in kata_kalimat:
        # Jika kata terpendek belum ditentukan atau panjangnya lebih kecil dari kata sekarang
        if kata_terpendek is None or len(kata) < len(kata_terpendek):
            kata_terpendek = kata
        # Jika kata terpanjang belum ditentukan atau panjangnya lebih besar dari kata sekarang
        if kata_terpanjang is None or len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata
    # Menampilkan hasil jika kalimat mengandung kata
    if kata_terpendek is not None and kata_terpanjang is not None:
        print("Kata terpendek: ", kata_terpendek)
        print("Kata terpanjang: ", kata_terpanjang)
    # Menampilkan pesan jika kalimat tidak mengandung kata
    else:
        print("Kalimat tidak mengandung kata")

# Contoh penggunaan program
kalimat = input("Masukkan kalimat: ")
kata_terpendek_terpanjang(kalimat)
