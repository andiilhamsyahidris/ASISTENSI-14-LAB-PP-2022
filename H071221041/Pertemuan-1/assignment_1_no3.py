print("Menghitung jumlah tagihan untuk pemakaian listrik bulanan")
print("=========================================================")

nilai = float(input("Rata-rata pemakaian listrik harian (wh):"))
tarif = 1325

harian = float(nilai/1000) #ubah wh ke kwh
bulanan = float(harian*30)
harga = float(bulanan*tarif)

print("Jumlah tagihan listrik bulanan: Rp.", round(harga,2))