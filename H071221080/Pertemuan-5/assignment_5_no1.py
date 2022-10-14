# Program mengalikan dua buah matriks 2x2

a1 = int(input('Input nilai matriks pertama index 1,1: '))
b1 = int(input('Input nilai matriks pertama index 1,2: '))
c1 = int(input('Input nilai matriks pertama index 1,3: '))
d1 = int(input('Input nilai matriks pertama index 1,4: '))
a2 = int(input('Input nilai matriks kedua index 1,1: '))
b2 = int(input('Input nilai matriks kedua index 1,2: '))
c2 = int(input('Input nilai matriks kedua index 1,3: '))
d2 = int(input('Input nilai matriks kedua index 1,4: '))

matriks = [[[a1, b1],[c1, d1]],[[a2, b2],[c2, d2]]]

a3 = (matriks[0][0][0]*matriks[1][0][0]) + (matriks[0][0][1]*matriks[1][1][0])
c3 = (matriks[0][1][0]*matriks[1][0][0]) + (matriks[0][1][1]*matriks[1][1][0])

b3 = (matriks[0][0][0]*matriks[1][0][1]) + (matriks[0][0][1]*matriks[1][1][1])
d3 = (matriks[0][1][0]*matriks[1][0][1]) + (matriks[0][1][1]*matriks[1][1][1])

print(f'| {a1}, {b1} | x | {a2}, {b2} | = | {a3}, {b3} |')
print(f'| {c1}, {d1} |   | {c2}, {d2} |   | {c3}, {d3} |')