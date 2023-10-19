def hapus_spasi_berlebih(kalimat):
    i = 0
    while i < len(kalimat):
        if kalimat[i] == " ":
            j = i + 1
            while j < len(kalimat) and kalimat[j] == " ":
                j += 1
            if j > i + 1:
                kalimat = kalimat[:i] + " " + kalimat[j:]
            i = j
        else:
            i += 1
    if kalimat[0] == " ":
        kalimat = kalimat[1:]
    if kalimat[-1] == " ":
        kalimat = kalimat[:-1]
    return kalimat.replace("  ", " ")

kalimat = input("Masukkan kalimat: ")
kalimat_baru = hapus_spasi_berlebih(kalimat)
print("Kalimat setelah spasi berlebih dihapus: ", kalimat_baru)

