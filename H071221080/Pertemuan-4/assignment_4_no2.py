# Program Mengembalikan FBB (Faktor Pembagi Terbesar) Dari Dua Bilangan Inputan

print('---Menentukan FPB dua bilangan---')

a= int(input('Nilai a : '))
b= int(input('Nilai b : '))

def bilangan(a, b):
    if a>b:
        nilai_terkecil= b
    elif a<b:
        nilai_terkecil= a
    if a < 0:
        print(f'Nilai {a} dibulatkan ke positif')
        a*= -1
        nilai_terkecil= a
        print(f'Menjadi {a}')
    if b < 0:
        print(f'Nilai {b} dibulatkan ke positif')
        b*= -1
        nilai_terkecil= b
        print(f'Menjadi {b}')
    else:
        nilai_terkecil= a or b

    for i in range(1, nilai_terkecil+1):
        if (a % i == 0) and (b % i == 0):
            FPB= i

    return FPB

print(f'FPB {a, b} = {bilangan(a, b)}')