# mencari angka terbesar pada 3 angka

print('===========================')
print('Angka terbesar dari 3 angka')
print('Rezqia Nurqalbi')
print('H071221025')
print('===========================')

a = int(input('Masukkan nilai a: '))
b = int(input('Masukkan nilai b: '))
c = int(input('Masukkan nilai c: '))

if a > b and a > c:
    print('A yang terbesar')
elif b > a and b > c:
    print('B yang terbesar')
else:
    print('C yang terbesar')
    