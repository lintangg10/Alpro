def belah_ketupat(n):
    # membuat bagian atas belah ketupat
    for i in range(n):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        print()

    # membuat bagian bawah belah ketupat
    for i in range(n-1, 0, -1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()

n = int(input("Masukkan nilai n: "))
belah_ketupat(n)