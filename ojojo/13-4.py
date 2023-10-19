def hapus_karakter_bersebelahan(string):
    if len(string) <= 1:
        return string
    elif string[0] == string[1]:
        i = 2
        while i < len (string) and string[i] == string[0]:
            i += 1
        return hapus_karakter_bersebelahan(string[1:])
    else:
        return string[0] + hapus_karakter_bersebelahan(string[1:])

string = 'aabbbcccdddeeefffgggg'
hasil_string = hapus_karakter_bersebelahan(string)
print(hasil_string)