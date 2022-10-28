# Menyalin nama, nim, dan angkatan ke dalam file txt

filename = input('Masukkan nama file : ') + ".txt"
n = int(input('Jumlah asisten : '))

listname = []
listnim = []
listangkatan = []

for i in range (n):
    nama = input('Masukkan nama : ')
    listname.append(nama)
    nim = input('Masukkan nim : ')
    listnim.append(nim)
    angkatan = int (input('Masukkan angkatan : '))
    listangkatan.append(angkatan)

check_len = len(listname[0])
for x in listname:
    if len(x) > check_len:
        check_len = len(x)

with open (filename, 'w') as file:
    if len(nama) < 20:
        file.write('+' + ('-' * (check_len + 2)) + '+' + ('-' * (12)) + '+' + ('-' * (10)) + '+\n')
        file.write('|' + ' Nama' + (' ' * ((check_len - 5) + 2)) + '|' + ' NIM' + (' ' * (8)) + '|' + ' Angkatan' + (' ' * (1)) + '|\n')
        file.write('+' + ('-' * (check_len + 2)) + '+' + ('-' * (12)) + '+' + ('-' * (10)) + '+\n')
        for i in range (n):
            file.write('|' + f'{listname[i]}' + (' ' * ((check_len - len(listname[i])) + 2)))
            file.write('|' + f'{listnim[i]}' + (' ' * (10)))
            file.write('|' + f'{listangkatan[i]}' + (' ' * (8)) + '|\n')
                    
        file.write('+' + ('-' * (check_len  + 2)) + '+' + ('-' * (12)) + '+' + ('-' * (10)) + '+\n')
        print('Berhasil')
    else:
        print('Gagal')
