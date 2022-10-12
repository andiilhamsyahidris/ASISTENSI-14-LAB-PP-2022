harga = int (input ("Harga :"))
bayar = int (input ("Bayar :"))
kembalian = bayar-harga
print ("Kembalian anda %d dengan rincian :" %(kembalian))
list = [100000,50000,20000,10000,5000,2000,1000,500,200,100]
if bayar>=harga : 
    for i in list :
        nilai= kembalian//i
        print ("%d uang Rp. %d" %(nilai,i))
        kembalian -= nilai*i
else :
    print ("Jumlah uang yang anda bayar tidak cukup")