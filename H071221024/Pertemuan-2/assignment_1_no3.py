#Menghitung jumlah angka-angka yang merupakan bilangan genap,ganjil,positif, dan negatif
try :
    a1,a2,a3,a4,a5 = map(int, input().split())
    x=[a1,a2,a3,a4,a5]

    genap=0
    jumlahganjil=0
    jumlahBilanganPositif=0
    jumlahBilanganNegatif=0

    if x[0]%2==0 :
        genap+=1
    elif x[0]%2==1 :
        jumlahganjil+=1
    if x[0]>0 :
        jumlahBilanganPositif+=1
    elif x[0]<0 :
        jumlahBilanganNegatif+=1
    if x[1]%2==0 :
        genap+=1
    elif x[1]%2==1 :
        jumlahganjil+=1
    if x[1]>0 :
        jumlahBilanganPositif+=1
    elif x[1]<0 :
        jumlahBilanganNegatif+=1
    if x[2]%2==0 :
        genap+=1
    elif x[2]%2==1 :
        jumlahganjil+=1
    if x[2]>0 :
        jumlahBilanganPositif+=1
    elif x[2]<0 :
        jumlahBilanganNegatif+=1
    if x[3]%2==0 :
        genap+=1
    elif x[3]%2==1 :
        jumlahganjil+=1
    if x[3]>0 :
        jumlahBilanganPositif+=1
    elif x[3]<0 :
        jumlahBilanganNegatif+=1
    if x[4]%2==0 :
        genap+=1
    elif x[4]%2==1 :
        jumlahganjil+=1
    if x[4]>0 :
        jumlahBilanganPositif+=1
    elif x[4]<0 :
        jumlahBilanganNegatif+=1
    print(genap,'Angka Genap')
    print(jumlahganjil,'Angka Ganjil')
    print(jumlahBilanganPositif,'Angka Positif')
    print(jumlahBilanganNegatif,'Angka negatif')
except :
    print('Inputan tidak valid')