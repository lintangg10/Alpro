import re
import random

def proses_email(email):
    email_split = email.split('@')
    return (email_split[0], email_split[1])

def proses_email_regex(email):
    pattern = r'(.+)@(.+)'
    hasil = re.search(pattern,email)
    return hasil

def generate_password(panjang):
    karakter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = " " 
    for _ in range (panjang):
        if password:
            passw = re.search(r'[a-zA-Z0-9]', password[::1])
            if passw is not None:
                password += karakter[ord(passw.group(0)) % 62]
            else:
                password += random.choice(karakter)
        else:
            password += random.choice(karakter)
    return password

#input user
email = input('masukkan email: ')
hasil = proses_email_regex(email)

print(f'Username: {hasil.group(1)}')
print(f'Hostname: {hasil.group(2)}')

username = hasil.group(1)
password = generate_password(8)

print(f'Password: {password}')
    
