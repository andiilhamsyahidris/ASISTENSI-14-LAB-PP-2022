#

n = int(input('n = '))

a1, a2 = 0, 1

for i in range(n): 
    i = a1
    a1 = a1 + a2
    a2 = a1 - a2
    print(i, end= ' ')