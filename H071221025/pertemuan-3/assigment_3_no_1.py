x = int(input("masukkan angka: "))
y = int(input("masukkan angka: "))

for i in range(1, y+1):
    print(i, end=" ")
    if i % x == 0 :
        print()