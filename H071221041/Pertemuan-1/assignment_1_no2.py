print("program ubah detik ke format jam:menit:detik")
print("============================================")

detik = int(input("Masukkan jumlah detik: "))

jam = detik//3600;
sisa_detik = detik%3600;
menit = sisa_detik//60;
detik = sisa_detik%60;
print("detik = ",jam,"Jam,",menit,"Menit,",detik,"Detik")