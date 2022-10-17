#mencari nilai duplikat

array_pertama = set(map(int, input('input array ke 1: ').split()))
array_kedua = set(map(int, input('input array ke 2: ').split()))

duplikat = tuple(array_pertama & array_kedua)
print(f"Terdapat {len(duplikat)} buah duplikat yaitu {duplikat}")