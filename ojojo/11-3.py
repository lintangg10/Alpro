dictionary_hours = {}
fname = input("Masukkan Nama File: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("File Tidak Bisa Dibuka:", fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 6 or words[0] != "From":
        continue
    else:
        email_time = words[5].split(':')
        hour = email_time[0]
        if hour not in dictionary_hours:
            dictionary_hours[hour] = 1
        else:
            dictionary_hours[hour] += 1

for hour, count in sorted(dictionary_hours.items()):
    print(hour, count)
