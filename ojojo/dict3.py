data=[
    {'V': 'S001'},
    {'V': 'S002'},
    {'VI': 'S001'},
    {'VI': 'S005'},
    {'VII': 'S005'},
    {'V': 'S009'},
    {'VIII': 'S007'},
]
hasil = [] #list
for d in data: #looping isi list
    for value in d.values(): #ambil value
        if hasil.count(value)==0: #jika belum ada di list, maka append
            hasil.append(value)

print(hasil)   
