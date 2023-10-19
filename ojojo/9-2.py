def deret_aritmatika(a, b, n):
    # Menghitung deret aritmatika
    deret = [a]
    for i in range(1, n):
        deret.append(deret[i-1] + b)
    return deret

# Input dari user
a = int(input("Nilai awal: "))
b = int(input("Beda: "))
n = int(input("Jumlah bilangan dalam deret: "))

# Percabangan untuk memastikan jumlah bilangan dalam deret lebih dari 0
if n > 0:
    # Menghitung dan menampilkan deret aritmatika
    deret = deret_aritmatika(a, b, n)
    print("Hasil deret aritmatika: ".format(a, b, n))
    i = 0
    while i < len(deret):
        print(deret[i], end=" ")
        i += 1
else:
    print("Jumlah bilangan dalam deret harus lebih dari 0.")

