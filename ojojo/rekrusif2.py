def sum_looping(n): #1+2+3+4+5+....+n=?
    hasil = 0
    for i in range(1, n+1):
        hasil = hasil + i
    return hasil

def sum_rumus(n): # (1+n)*(n/2)
    return int ((1+n)*(n/2))

def sum_rekrusif(n):
    if n ==1:
        return 1
    else: 
        return sum_rekrusif(n-1) + n

print(sum_looping(17))
print(sum_rumus(17))
print(sum_rekrusif(17))