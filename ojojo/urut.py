#cetak(5,9)=>5,6,7,8,9
#cetak (18,14)=> 14, 15,16,17,18
def cetak(a,b):
    if a >= b:
        for i in range(b,a+1):
            print(i)
    else:
        for i in range(a, b+1):
            print(i)

#main
cetak(5,9)