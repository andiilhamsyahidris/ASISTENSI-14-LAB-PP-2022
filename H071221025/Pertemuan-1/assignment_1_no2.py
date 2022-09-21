#konversi waktu

nilai = int(input("detik : "))

jam = nilai // 3600;
sisa_detik = nilai%3600;
menit = sisa_detik//60;
detik = sisa_detik%60;

print(f" j:m:d => {jam}:{menit}:{detik}")
