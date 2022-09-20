konversi = int (input ('masukkan detik :'))
jam = konversi//3600
jjam = konversi%3600
menit = jjam//60
detik = jjam%60

print ("%d:%d:%d", (jam,menit,detik))