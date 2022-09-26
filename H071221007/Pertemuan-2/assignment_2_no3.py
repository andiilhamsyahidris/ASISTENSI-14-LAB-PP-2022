a = int (input ("Masukkan nilai a :"))
b = int (input ("Masukkan nilai b :"))
c = int (input ("Masukkan nilai c :"))
if (a>=b and a>=c) :
    print ("> %d adalah nilai terbesar" %(a))
elif b>=a and b>=c :
    print ("> %d adalah nilai terbesar" %(b))
else :
    print ("> %d adalah nilai terbesar" %(c))