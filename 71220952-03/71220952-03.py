#input
bil1 = int(input('bil1: '))
bil2 = int(input('bil2: '))
bil3 = int(input('bil3: '))

#proses
if bil1 % 10 >= 5:
    bulat_bil1 = ((bil1 // 10) + 1) * 10
else:
    bulat_bil1 = (bil1 // 10) * 10

if bil2 % 10 >= 5:
    bulat_bil2 = ((bil2 // 10) + 1) * 10
else:
    bulat_bil2 = (bil2 // 10) * 10

if bil3 % 10 >= 5:
    bulat_bil3 = ((bil3 // 10) + 1) * 10
else:
   bulat_bil3 = (bil3 // 10) * 10

total = bulat_bil1 + bulat_bil2+ bulat_bil3

# output
print("Maka jawabannya adalah ",total )