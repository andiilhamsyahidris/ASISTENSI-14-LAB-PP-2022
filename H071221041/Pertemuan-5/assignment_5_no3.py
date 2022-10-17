arrayPertama=set(map(int,input('input array1:').split()))
arrayKedua=set(map(int,input('input array2:').split()))

duplikat= tuple(arrayPertama & arrayKedua)
print(f"Terdapat {len(duplikat)} buah duplikat yaitu",duplikat)
