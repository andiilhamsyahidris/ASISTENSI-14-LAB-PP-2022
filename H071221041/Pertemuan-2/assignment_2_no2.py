print('MENGHITUNG TAGIHAN  LISTRIK')
print('  Andi Muthia Mulia Putri  ')
print('===========================')

golongan=(input('Golongan = '))
daya=int(input('Daya = '))
pemakaian=int(input('Pemakaian = '))

if golongan=='R1' and daya == 900:
    tarif= 1352
    tagihan=tarif*pemakaian
    print('Jumlah tagihan anda: Rp.', tagihan)
elif golongan=='R1' and 1300 <=daya <= 2200:
    tarif= 1444.70
    tagihan=tarif*pemakaian
    print('Jumlah tagihan anda: Rp.', tagihan)
elif golongan=='R2' and 3500<= daya <=5500:
    tarif= 1699.53
    tagihan=tarif*pemakaian
    print('Jumlah tagihan anda: Rp.', tagihan)
elif golongan=='R3' and daya >= 6600:
    tarif= 1699.53
    tagihan=tarif*pemakaian
    print('Jumlah tagihan anda: Rp.', tagihan)
elif golongan=='B2' and 6600 <= daya <=200000:
    tarif= 1444.70
    tagihan=tarif*pemakaian
    print('Jumlah tagihan anda: Rp.', tagihan)
elif golongan=='B3' and daya >=200000:
    tarif= 1114.74
    tagihan=tarif*pemakaian
    print('Jumlah tagihan anda: Rp.', tagihan)
elif golongan=='I3' and daya >=200000:
    tarif= 1314.12
    tagihan=tarif*pemakaian
    print('Jumlah tagihan anda: Rp.', tagihan)
elif golongan=='P1' and 6600 <=daya <=200000:
    tarif= 1523.28
    tagihan=tarif*pemakaian
    print('Jumlah tagihan anda: Rp.', tagihan)
else:
    print('data tidak valid ')
