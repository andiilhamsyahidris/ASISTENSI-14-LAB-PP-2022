#Piramid * dari inputan X

X = int(input("masukkan jumlah baris: "))

for i in range(X):
    for j in range(X - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()