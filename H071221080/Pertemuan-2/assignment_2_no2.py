# program menghitung total tagihan listrik

try :
    golongan= str(input('Golongan = '))
    daya= int(input('Daya = '))
    pemakaian= int(input('Pemakaian = '))

    if golongan == 'R1':
        if daya == 900:
            tarif= 1352
        elif daya == 1300:
            tarif= 1444.70
        elif daya == 2200:
            tarif= 1444.70

    elif golongan == 'R2':
        if daya >= 3500 and daya <= 5500:
            tarif= 1699.53

    elif golongan == 'R3':
        if daya >= 6600:
            tarif= 1699.53

    elif golongan == 'B2':
        if daya >= 6600 and daya <= 200000:
            tarif= 1444.70

    elif golongan == 'B3':
        if daya > 200000:
            tarif= 1114.74

    elif golongan == 'I3':
        if  daya >= 200000:
            tarif= 1314.12

    elif golongan == 'P1':
        if daya >= 6600 and daya <= 200000:
            tarif= 1523.28

    tagihan= tarif * pemakaian
    print('Jumlah tagihan anda sebesar : Rp.', tagihan)

except :
    print('---Data tidak valid---')
    print('-> Golongan atau Daya yang diinput tidak sesuai')