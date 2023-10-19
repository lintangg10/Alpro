def palindrome_perulangan(input_string):
    input_string = input_string.lower()
    reversed_input_string = input_string[::-1]
    if input_string == reversed_input_string:
        return True
    else:
        return False
    
def paldrome_rekrusif(input_string, depan, belakang):
    ##base case jika karakter hanya 1
    if depan == belakang:
            return True
    #base case jika bersebelahan karakter tinggal 2
    elif belakang == depan + 1:
        if input_string[depan] == input_string[belakang]:
              return True
        else:
             return False
    else:
         if input_string[depan]==input_string[belakang]:
              return paldrome_rekrusif(input_string, depan+1, belakang-1)
         else:
              return False


    
print(palindrome_perulangan('kaSur rusak'))
print(palindrome_perulangan('praktikum alpro'))

kalimat = 'KaSur RuSAk'
print(paldrome_rekrusif(kalimat.lower(), 0, len(kalimat)-1))

kalimat = 'praktikum alpro'
print(paldrome_rekrusif(kalimat.lower(), 0, len('praktikum alpro')-1))