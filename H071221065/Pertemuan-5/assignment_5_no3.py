# Mencari duplikat dari 2 buah array
 
set_a = set(map (int, input("Input Array ke 1: ").split()))
set_b = set(map (int, input("Input Array ke 2: ").split()))

tup_a = tuple(set_a & set_b)

print(f'Terdapat {len(set_a & set_b)} buah duplikat yaitu, {tup_a},')