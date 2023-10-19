batas_bawah = int(input('masukkan batas bawah: '))
batas_atas = int(input('masukkan batas atas: '))

if batas_bawah > batas_atas:
    for i in range(batas_bawah, batas_atas -1, -1):
         if i % 2 == 1:
             if i == batas_atas or i == batas_atas + 1:
                 print(i)
         else: 
             print(i, end=",")

else:
    for i in range(batas_bawah, batas_atas + 1):
        if i % 2 == 1:
            if i == batas_atas or i == batas_atas - 1:
                print(i)
        else:
            print(i, end=",")


