# # # #faktorial genap

# # # def faktorialgenap(jumlah, awal):
# # #     #base case
# # #     if jumlah == 0 :
# # #         return 1
# # #     else : 
# # #         #recursive case
# # #         return faktorialgenap(jumlah-1, awal+2) * (awal+2)
    

# # # #print (faktorialgenap(5, 0)) => 2*4*6*8*10
# # # print(faktorialgenap(5,0))

# # def cekprima(n, divisor=0, result=True):
# #     if n <= 1:
# #         return False
# #     elif n == 2:
# #         return True
# #     elif divisor == 1:
# #         return result
# #     else:
# #         if divisor == 0:
# #             divisor = n-1
# #         if (n%divisor == 0):
# #             result = result and False
# #         else:
# #             result = result and True
# #         return cekprima(n, divisor-1, result)       
# # def cariangka(n):
# #     sum = 0
# #     jumlah_prima_found = 0
# #     iterate = 1
# #     while jumlah_prima_found < n:  
# #         if (cekprima(iterate)):
# #             jumlah_prima_found +=1
# #             sum += iterate
# #         iterate += 1
# #     return sum
# # print(cariangka(2))

# def binary_to_dex(biner, pangkat=0):
#     if biner == '0':
#         return 0
#     elif biner == '1':
#         return pow (2, pangkat)
#     else:
#         last_digit =int (biner[-1])
#         if last_digit == 0:
#             return binary_to_dex(biner[:-1], pangkat + 1)
#         else:
#             return binary_to_dex(biner[:-1], pangkat +1) + (last_digit*2)**pangkat
        
# def bagibiner(biner):
#     pecahan = biner.split('.')
#     for i in range(len(pecahan)):
#         pecahan[i] = binary_to_dex(pecahan[i])
#     hasil = f'{pecahan[0]}.{pecahan[1]}.{pecahan[2]}.{pecahan[3]}'
#     return hasil

# print(bagibiner("11000000.10101000.00000001.00000001"))
# print(bagibiner("11000000.10101000.00000001.00000010"))

# print(bagibiner("00001010.00001010.00001010.00001010"))