x = int(input("masukkan angka: "))

a1 = 0
a2 = 1


for i in range(x):
    print(a1, end=' ')
    n = a2 + a1
    a1 = a2
    a2 = n
    
    