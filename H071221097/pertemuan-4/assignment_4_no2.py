# Menghitung FPB dari dua inputsn angka integer

def fpb (x,y) :
    if (y == 0) :
        return x
    else :
        return fpb (y,x % y)

x = int(input("masukkan bilangan pertama: "))
y = int(input("masukkan bilangan kedua: "))
print("FPB dari", x,"dan", y, "=",fpb (x,y))

