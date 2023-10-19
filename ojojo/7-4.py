def kata_terpendek_terpanjang(kalimat): 
    kata_terpendek = None
    kata_terpanjang = None
    kata_kalimat = kalimat.split()
    for kata in kata_kalimat:
        if kata_terpendek is None or len(kata) < len(kata_terpendek):
            kata_terpendek = kata
        if kata_terpanjang is None or len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata
    if kata_terpendek is not None and kata_terpanjang is not None:
        print("Kata terpendek: ", kata_terpendek)
        print("Kata terpanjang: ", kata_terpanjang)
    else:
        print("Kalimat tidak mengandung kata")

kalimat = input("Masukkan kalimat: ")
kata_terpendek_terpanjang(kalimat)
