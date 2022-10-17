#Program Mencari Nilai Duplikat 2 Array

set_1 = set(map(int, input("Input Array ke 1:").split()))
set_2 = set(map(int, input("Input Array ke 2:").split()))

tup_irisan = tuple (set_1 & set_2)

print (f'Terdapat {(len(tup_irisan))} buah duplikat yaitu {tup_irisan}')
