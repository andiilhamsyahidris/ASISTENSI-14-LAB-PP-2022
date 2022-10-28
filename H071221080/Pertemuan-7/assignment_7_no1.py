# Program mengecek sebuah string S apakah sesuai
# dengan kondisi dalam soal

import re
s = input('')

# MENYETEL REGULAR EXPRESSION
regex_space = r'\s'
regex_digit = r'\d'
regex_alphabet = r'[A-Z,a-z]'

# MENENTUKAN APAKAH 40 KARAKTER PERTAMA MEMENUHI KONDISI
result1 = re.findall(regex_space, s[0:40])
if result1:
    print('false')
    exit()

result1_digit = re.findall(regex_digit, s[0:40])
for i in result1_digit:
    i = int(i)
    if i % 2 == 1:
        print('false')
        exit()

# MENENTUKAN APAKAH KARAKTER KE-41 SAMPAI 45 MEMENUHI KONDISI
result2 = re.findall(regex_alphabet, s[40:45])
if result2:
    print('false')
    exit()

result2_digit = re.findall(regex_digit, s[40:45])
for j in result2_digit:
    j = int(j)
    if j % 2 == 0:
        print('false')
        exit()

# MENENTUKAN APAKAH JUMLAH KARAKTER ATAU PANJANG STRING MEMENUHI KONDISI
if len(s) == 45:
    print('true')
else:
    print('false')
    exit()