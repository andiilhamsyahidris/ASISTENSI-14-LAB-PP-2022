print('=====================')
print('total tagihan listrik')
print('=====================')
golongan = (input('golongan :')).upper()
daya = int(input('daya :'))
pemakaian = int(input('pemakaian : '))
if golongan == 'R1' :
    if daya == 900 :
        tagihan = (pemakaian*1352)
        print(f'Jumlah tagihan anda: {tagihan}')
    elif daya == 1300 :
        tagihan = (pemakaian*1444.70)
        print(f'Jumlah tagihan anda: {tagihan}')
    elif daya == 2200 :
        tagihan = (pemakaian*1444.70)
        print(f'Jumlah tagihan anda: {tagihan}')
    else :
        print ('data tidak valid')
if golongan == 'R2' :
    if daya >= 3500 and daya <=5500 :
        tagihan = (pemakaian*1699.53)
        print(f'Jumlah tagihan anda: {tagihan}')
    else :
        print ('data tidak valid')
if golongan == 'R3' :
    if daya >= 6600 :
        tagihan = (pemakaian*1699.53)
        print(f'Jumlah tagihan anda: {tagihan}')
    else : 
        print ('data tidak valid')
if golongan == 'B2' :
    if daya >= 6600 and daya <=200000 :
        tagihan = (pemakaian*1444.70)
        print(f'Jumlah tagihan anda: {tagihan}')
    else :
        print ('data tidak valid')
if golongan == 'B3' :
    if daya >= 200000 :
        tagihan = (pemakaian*1444.74)
        print(f'Jumlah tagihan anda: {tagihan}')
if golongan == 'I3' :
    if daya >=200000 :
        tagihan = (pemakaian*1314.12)
        print(f'Jumlah tagihan anda: {tagihan}')
    else : 
        print ('data tidak valid')
if golongan == 'P1' :
    if daya >=6600 and daya <=200000 :
        tagihan = (pemakaian*1523.28)
        print(f'Jumlah tagihan anda: {tagihan}')
    else : 
        print ('data tidak valid')
else:
    print('Data tidak valid')
# print (f'jumlah tagihan anda :{tagihan}')

