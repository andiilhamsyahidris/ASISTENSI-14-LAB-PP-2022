# menentukan panjang kapal jika dilihat dari menara

import math

print('---Semua inputan angka di bawah dinyatakan dalam satuan meter (m)---')
h= int(input('Ketinggian menara : '))
a= int(input('Sudut elevasi terhadap ujung depan kapal : '))
b= int(input('Sudut elevasi terhadap ujung belakang kapal : '))

a1= math.radians(a)
a2= math.tan(a1)
a3= a2 * h

b1= math.radians(b)
b2= math.tan(b1)
b3= b2 * h

hasil1= a3-b3
hasil2= round(hasil1, 1)
print('Panjang kapal adalah : ', hasil2, 'm')