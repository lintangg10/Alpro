def hitung_kemunculan_kata(kalimat, kata):

    if not isinstance(kalimat, str) or not isinstance(kata, str):
        return "Input harus berupa string"
    
    kalimat = kalimat.lower()
    kata = kata.lower()
    
    kalimat = kalimat.replace(" ", "")
 
    frekuensi = 0
    for i in range(len(kalimat) - len(kata) + 1):
        if kalimat[i:i+len(kata)] == kata:
            frekuensi += 1
   
    return "Kata '{}' muncul sebanyak {} kali pada kalimat.".format(kata, frekuensi)

kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang ingin dihitung frekuensinya: ")
print(hitung_kemunculan_kata(kalimat, kata))
