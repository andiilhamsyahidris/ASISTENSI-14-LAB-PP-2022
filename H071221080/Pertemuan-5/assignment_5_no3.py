# Program yang mencari duplikat dari 2 buah array

a = set(map(int, input('Input array ke 1: ').split()))
b = set(map(int, input('Input array ke 2: ').split()))

duplikat = tuple(a & b)

print(f'Terdapat {len(duplikat)} buah duplikat yaitu {duplikat}')