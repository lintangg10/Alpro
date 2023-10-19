khs = {
    '71200183' : ['tekkom', 'jarkom', 'logmat',],
    '71193450' : ['PAK', 'Tekkkom', 'Logmat']
}

# print(khs['71193450'])
for key in khs.keys():
    print(f'NIM: {key}, Matkul: {khs[key]}')

print()

khs['71193450'].append('IMK')
print(khs)

del khs['71200183'][0]

print(khs)