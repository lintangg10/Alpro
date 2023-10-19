nama_file = 'soal.txt'
handle = open (nama_file, 'r') 
isi_file = handle.readlines()
isi_file = [line.lower() for line in isi_file]
handle.close()

for line in isi_file:
    soal, jawaban = line.strip().split('||')
    jawaban_user = input(soal + '\nJawab: ')
    if jawaban_user.strip().lower() == jawaban.strip().lower():
        print('Jawaban benar!\n')
    else:
        print('Jawaban salah. Jawaban benar yaitu: ', jawaban, '\n')