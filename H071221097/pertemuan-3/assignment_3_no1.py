x = int(input("masukkan x= "))
y = int(input("masukkan y= "))

while x > y:
    print("ingat y harus lebih besar dari x, harap ulangi masukan.")
    x = int(input("masukkan x= "))
    y = int(input("masukkan y= "))

for i in range(1, y+1):
    print(f'{i} ', end=" ")
    if i % x == 0:
        print()
