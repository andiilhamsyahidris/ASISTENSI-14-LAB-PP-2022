nilai = float (input("Rata-rata pemakaian listrik harian (wh): "))
tarif = 1325  # Dalam kWh


harian = float(nilai/1000) #mengubah wh ke Kwh
bulanan = float(harian * 30)
harga = float(bulanan * tarif)

print("Jumlah tagihan listrik bulanan : Rp.", round(harga , 2))
