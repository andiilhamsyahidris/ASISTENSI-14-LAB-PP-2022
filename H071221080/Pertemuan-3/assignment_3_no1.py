#

x = int(input('Nilai x : '))
y = int(input('Nilai y : '))

for i in range(1, y+1):
    print(i, end= ' ')
    if i % x == 0:
        print()