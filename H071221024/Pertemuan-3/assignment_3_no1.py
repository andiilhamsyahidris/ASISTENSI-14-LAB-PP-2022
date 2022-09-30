x=int(input('Masukkan nilai x: '))
y=int(input('Masukkan nilai y: '))

for i in range(1,y+1) :
    print(i, end=" ")
    if i%x==0 :
        print()
