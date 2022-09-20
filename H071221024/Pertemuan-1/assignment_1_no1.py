import math
print('Menghitung panjang kapal')

h = int(input("Ketinggian menara: "))
a = int(input("Sudut elevasi ujung belakang kapal: "))
b = int(input("Sudut elevasi ujung depan kapal: "))

a = math.tan(math.radians(a))*h
b = math.tan(math.radians(b))*h

Panjang_kapal = a-b
Panjang_kapal = round(Panjang_kapal, 1)
print("Panjang kapal: ",Panjang_kapal, 'm')