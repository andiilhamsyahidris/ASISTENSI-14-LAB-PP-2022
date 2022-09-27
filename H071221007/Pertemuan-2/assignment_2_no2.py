golongan = input ("Golongan (R1/R2/R3/B2/B3/I3/P1) :")
daya = int (input ("Masukkan Daya :"))
pemakaian = int (input("Masukkan Pemakaian :"))
if golongan == "R1" :
    if daya == 900 : 
        print ("> jumlah tagihan anda :",round(pemakaian*1352,1))
    elif daya == 1300 :
        print ("> jumlah tagihan anda :",round(pemakaian*1444.7,1))
    elif daya == 2200 :
        print ("> jumlah tagihan anda :",round(pemakaian*1444.7,1))
    else :
        print ("jumlah daya yang anda masukkan tidak sesuai dengan golongan %s" %(golongan))
elif golongan == "R2" :
    if daya >= 3500 <= 5500 :
        print ("> jumlah tagihan anda :",round(pemakaian*1699.53,1))
    else :
        print ("jumlah daya yang anda masukkan tidak sesuai dengan golongan %s" %(golongan))
elif golongan == "R3" :
    if daya >= 6600 :
        print ("> jumlah tagihan anda :",round(pemakaian*1699.53,1))
    else :
        print ("jumlah daya yang anda masukkan tidak sesuai dengan golongan %s" %(golongan))
elif golongan == "B2" :
    if daya >= 6600 <= 200000 :
        print ("> jumlah tagihan anda :",round(pemakaian*1444.7,1))
    else :
        print ("jumlah daya yang anda masukkan tidak sesuai dengan golongan %s" %(golongan))
elif golongan == "B3" :
    if daya > 200000 :
        print ("> jumlah tagihan anda :",round(pemakaian*1114.74,1))
    else :
        print ("jumlah daya yang anda masukkan tidak sesuai dengan golongan %s" %(golongan))
elif golongan == "I3" :
    if daya >= 200000 :
        print ("> jumlah tagihan anda :",round(pemakaian*1314.12,1))
    else :
        print ("jumlah daya yang anda masukkan tidak sesuai dengan golongan %s" %(golongan))
elif golongan == "P1" :
    if daya >= 6600 <= 200000 :
        print ("> jumlah tagihan anda :",round(pemakaian*1523.28,1))
    else : 
        print ("jumlah daya yang anda masukkan tidak sesuai dengan golongan %s" %(golongan))
else :
    print ("golongan %s tidak memenuhi" %(golongan))

