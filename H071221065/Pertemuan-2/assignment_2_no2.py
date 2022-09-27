#Menghitung daya listrik dan total tagihan listrik 

Golongan = input("Golongan Listrik: ")
Daya = int(input("Daya Listrik: "))
Pemakaian = int(input("Pemakaian: "))

if Golongan == "R1":
    if Daya == 900:
        print(f"jumlah tagihan anda: Rp {Pemakaian * 1352}")
    elif Daya == 1300 :
        print(f"Jumlah tagihan anda: Rp {Pemakaian * 1444.70}")
    elif Daya == 2200 :
        print(f"Jumlah tagihan anda: Rp {Pemakaian * 1444.70}")
    else :
        print("Data tidak valid")
elif Golongan == "R2":
    if Daya >= 3500 and Daya <= 5500 :
        print(f"jumlah tagihan anda: Rp {Pemakaian * 1699.53}")
    else :
        print("Data tidak valid")
elif Golongan == "R3":
    if Daya >= 6600 :
        print(f"jumlah tagihan anda: Rp {Pemakaian * 1699.53}")
    else :
        print("Data tidak valid")
elif Golongan == "B2":
    if Daya >= 6600 and Daya <= 200000 :
        print(f"jumlah tagihan anda: Rp {Pemakaian * 1444.70}")
    else :
        print("Data tidak valid")
elif Golongan == "B3":
    if Daya >= 2000000 :
        print(f"jumlah tagihan anda: Rp {Pemakaian * 1114.74}")
    else :
        print("Data tidak valid")
elif Golongan == "I3":
    if Daya >= 2000000 :
        print(f"jumlah tagihan anda: Rp {Pemakaian * 1314.12}")
    else :
        print("Data tidak valid")

elif Golongan == "P1":
    if Daya >= 6600 and Daya <= 200000 :
        print(f"jumlah tagihan anda: Rp {Pemakaian * 1523.28}")
    else :
        print("Data tidak valid")
else:
    print('Data tidak valid')