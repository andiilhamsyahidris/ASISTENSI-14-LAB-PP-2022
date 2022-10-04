x=int(input("masukkan nilai:"))
a,b=0,1

for i in range(x):
    print(f'perulangan ke - {i}')
    print(a, end=" ")
    n=a+b
    a=b
    b=n
    print (n)

    