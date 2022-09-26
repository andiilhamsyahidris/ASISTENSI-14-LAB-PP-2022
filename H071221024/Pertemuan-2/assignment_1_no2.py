#Menginput informasi daya listrik dan menghitung total tagihan listrik
golongan=str(input('golongan = '))
daya=int(input('daya = '))
pemakaian=int(input('pemakaian dalam jam = '))

if golongan == 'R1' :
    if daya == 900 :
        tarifKwh=1352
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    elif daya == 1300 :
        tarifKwh=1444.70
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    elif daya == 2200 :
        tarifKwh=1444.70
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    else :
        print(f'daya listrik {daya} VA tidak terdaftar pada golongan {golongan}, coba masukkan dan mengecek kembali daya listrik anda')
elif golongan == 'R2' :
    if daya >=3500 and daya <=5500 :
        tarifKwh=1699.53
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    else :
        print(f'daya listrik {daya} VA tidak terdaftar pada golongan {golongan}, coba masukkan dan mengecek kembali daya listrik anda')
elif golongan == 'R3' :
    if daya >= 6600 :
        tarifKwh=1699.53
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    else :
        print(f'daya listrik {daya} VA tidak terdaftar pada golongan {golongan}, coba masukkan dan mengecek kembali daya listrik anda')
elif golongan == 'B2' :
    if daya >= 6600 and daya <= 200000 :
        tarifKwh=1444.70
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    else :
        print(f'daya listrik {daya} VA tidak terdaftar pada golongan {golongan}, coba masukkan dan mengecek kembali daya listrik anda')
elif golongan == 'B3' :
    if daya >= 200000 :
        tarifKwh=1114.74
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    else :
        print(f'daya listrik {daya} VA tidak terdaftar pada golongan {golongan}, coba masukkan dan mengecek kembali daya listrik anda')
elif golongan == 'I3' :
    if daya >= 200000 :
        tarifKwh=1314.12
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    else :
        print(f'daya listrik {daya} VA tidak terdaftar pada golongan {golongan}, coba masukkan dan mengecek kembali daya listrik anda')
elif golongan == 'P1' :
    if daya >= 6600 and daya <= 200000 :
        tarifKwh=1523.28
        jumlahTagihan=pemakaian*tarifKwh
        print(f'jumlah tagihan anda : Rp {jumlahTagihan:,}')
    else :
        print(f'daya listrik {daya} VA tidak terdaftar pada golongan {golongan}, coba masukkan dan mengecek kembali daya listrik anda')
else :
    print('golongan', golongan, 'tidak terdaftar pada aturan tarif, coba masukkan dan mengecek kembali golongan anda')