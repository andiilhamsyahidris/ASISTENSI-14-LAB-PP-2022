#Menentukan nilai terbesar dari tiga angka

a, b, c = int(input("a : ")), int(input("b : ")), int(input("c : "))
if a < b and c < b:
    print("%d adalah nilai terbesar" % (b))
elif a < c and b < c:
    print("%d adalah nilai terbesar" % (c))
else:
    print("%d adalah nilai terbesar" % (a))