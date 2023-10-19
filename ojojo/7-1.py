def anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()
 
    kata1 = kata1.replace(" ", "")
    kata2 = kata2.replace(" ", "")
   
    panjang_kata1 = len(kata1)
    panjang_kata2 = len(kata2)
   
    if panjang_kata1 != panjang_kata2:
        return False
   
    for karakter in kata1:
        if kata1.count(karakter) != kata2.count(karakter):
            return False
    return True

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
if anagram(kata1, kata2):
    print("Kedua kata adalah anagram")
else:
    print("Kedua kata bukan anagram")

