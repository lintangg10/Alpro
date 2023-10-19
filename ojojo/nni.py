def ternarySearch(l, r, key, ar):
    while r >= 1:
        mid1= l+ (r-1) // 3
        mid2 = r (r-1) // 3

        if key== ar[mid1]:
            return mid1

        if key == mid2:
            return mid2
        
        if key < ar[mid1]: 
            r = mid1 - 1
        elif key> ar[mid2]:
            l = mid2 + 1

        else:
            l = mid1 + 1 
            r = mid2 - 1 

    return -1

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 1
r=12
key=12