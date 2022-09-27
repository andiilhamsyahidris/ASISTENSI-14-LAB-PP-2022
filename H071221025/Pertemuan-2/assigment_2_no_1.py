#konversi angka ke huruf


print('==============================')
print('konversi Angka ke huruf')
print('Rezqia Nurqalbi')
print('H071221025')
print('==============================')

nilai = int(input('Masukkan Nilai : '))
if nilai >= 90:
    na = 'a'
elif nilai >= 80:
    na = 'b'
elif nilai >= 70:
    na = 'c'
elif nilai >= 60:
    na = 'd'
elif nilai >= 40:
    na = 'e'
else:
    na = 'f'
print(f'Nilai anda : {na}')
 
