#membuat program untuk menginput informasi daya listrik dan menghitung total tagihan listrik berdasarkan aturan

golongan = (input("Masukkan golongan Anda: "))
daya = float(input("Masukkan daya listrik Anda (VA): "))
pemakaian = float(input("Masukkan total pemakaian listrik Anda: "))

if golongan == 'R1':
    if daya == 900 :
        print (f"Jumlah tagihan Anda : {pemakaian*1352:,}")
    elif  1300 <= daya <= 2200 :
        print (f"jumlah tagihan anda : {pemakaian*1400.70:,}")
    else :
        print("Data tidak ditemukan")
elif golongan == 'R2':
    if 3500 <= daya <= 5500 :
        print (f"Jumlah tagihan Anda : {pemakaian*1699.53:,}")
    else :
        print("Data tidak ditemukan")
elif golongan == 'R3':
    if daya >= 6600 :
        print (f"Jumlah tagihan Anda : {pemakaian*1699.53:,}")
    else :
        print("Data tidak ditemukan")
elif golongan == 'B2':
    if   6600 <=  daya <= 200000 :
        print (f"Jumlah tagihan Anda : {pemakaian*1444.70:,}")
elif golongan == 'B3':
    if daya >= 20000 :
        print (f"Jumlah tagihan Anda : {pemakaian*1444.74:,}")
    else :
        print("Data tidak ditemukan")
elif golongan == 'I3':
    if daya >= 20000 :
        print (f"Jumlah tagihan Anda : {pemakaian*1314.12:,}")
    else :
        print("Data tidak ditemukan")
elif golongan == 'P1':
    if  6600 <= daya <= 200000 :
        print (f"Jumlah tagihan Anda : {pemakaian*1314.12:,}")
    else :
        print("Data tidak ditemukan!")
else:
    print("Data tidak ditemukan")