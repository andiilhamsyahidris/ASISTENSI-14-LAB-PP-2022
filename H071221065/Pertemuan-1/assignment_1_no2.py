detik  = int(input("masukkan detik: "))

jam = detik // 3600;
sisa_detik = detik % 3600;
menit = sisa_detik //60;
detik = sisa_detik % 60;


print("%d : %d : %d" % (jam,menit,detik))