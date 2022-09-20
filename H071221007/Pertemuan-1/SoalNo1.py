import math

tinggi = float (input ("masukkan nilai h :"))

sudut_a = float (input ('masukkan nilai a :'))

radA = (math.pi/180)*sudut_a
sudut_b = float (input ("masukkan nilai b :"))

radB = (math.pi/180)*sudut_b

sisi_depan = tinggi / math.tan (radA)
kapal_menara = tinggi / math.tan (radB)
panjang_kapal = sisi_depan - kapal_menara
print (round(panjang_kapal,1))