import math
print('Menghitung panjang kapal')

h=float(input("\nMasukkan nilai ketinggian menara:"))
a=float(input("Masukkan nilai sudut elevasi pengamat terhadap ujung belakang kapal:"))
b=float(input("Masukkan nilai sudut elevasi pengamat terhadap ujung depan kapal:"))


rad=(math.pi/180)*a
tan_a= math.tan(rad)

rad=(math.pi/180)*b
tan_b= math.tan(rad)

ac= tan_a*h
print(ac)
bc= tan_b*h
print(bc)
x=ac-bc
print(round(x,1))