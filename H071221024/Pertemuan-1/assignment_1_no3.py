from cmath import pi


import math

print('Menghitung volume dan luas permukan kerucut')

r=int(input('Jari-jari alas : '))
t=int(input('Tinggi : '))

sisi_miring=(t**2+r**2)**0.5

volume=1/3*pi*r**2*t
volume1=round(volume,2)
luas_Permukaan=pi*r*(r+sisi_miring)
luas_Permukaan1=round(luas_Permukaan,2)

print('Volume :', volume1)
print('Luas permukaan :', luas_Permukaan1)