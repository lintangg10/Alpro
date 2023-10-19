def perkalian(x, y):
    hasil = 0
    print(f'{x} X {y} = ', end="")
    for i in range(1, x+1): 
        if i == x:
            print(f'{y} =', end = "")
        else:
            print(f'{y} + ', end = "")
        hasil = hasil + y
    print(f'{hasil}')

perkalian(6,5)
perkalian(7,10)