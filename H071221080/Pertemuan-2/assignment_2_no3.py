# program mencari berapa angka positif, negatif, ganjil, dan genap

try :
    a, b, c, d, e = map(int, input('Masukkan lima angka (dalam bentuk sejajar): ').split())

    x= [a, b, c, d, e]

    genap= 0
    ganjil= 0
    positif= 0
    negatif= 0

    if x[0] % 2 == 0:
        genap+= 1
    elif x[0] % 2 == 1:
        ganjil+= 1
    if x[0] > 0:
        positif+= 1
    elif x[0] < 0:
        negatif+= 1

    if x[1] % 2 == 0:
        genap+= 1
    elif x[1] % 2 == 1:
        ganjil+= 1
    if x[1] > 0:
        positif+= 1
    elif x[1] < 0:
        negatif+= 1

    if x[2] % 2 == 0:
        genap+= 1
    elif x[2] % 2 == 1:
        ganjil+= 1
    if x[2] > 0:
        positif+= 1
    elif x[2] < 0:
        negatif+= 1

    if x[3] % 2 == 0:
        genap+= 1
    elif x[3] % 2 == 1:
        ganjil+= 1
    if x[3] > 0:
        positif+= 1
    elif x[3] < 0:
        negatif+= 1

    if x[4] % 2 == 0:
        genap+= 1
    elif x[4] % 2 == 1:
        ganjil+= 1
    if x[4] > 0:
        positif+= 1
    elif x[4] < 0:
        negatif+= 1

    print(f'{genap} Angka Genap')
    print(f'{ganjil} Angka Ganjil')
    print(f'{positif} Angka Positif')
    print(f'{negatif} Angka Negatif')

except :
    print('Inputan Tidak Valid')