print('konversi Huruf Ke Angka')
print('Andi Muthia MUlia Putri')
print('==============================')
nilai = int(input ('Masukkan nilai : '))

if nilai >= 90:
    indeks = 'A'
elif nilai >= 80:
    indeks = 'B'
elif nilai >= 70:
    indeks = 'C'
elif nilai >= 60:
    indeks = 'D'
elif nilai >= 40:
    indeks = 'E'
else:
    indeks = 'F'
print(f'Nilai {nilai} = {indeks}')