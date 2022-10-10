n=int(input('Masukkan bilangan bulat: '))
def faktorial(n) :
    if n==0 :
        return 1
    elif n>0 :
        return n*faktorial(n-1)
    else :
        return 'Tidak Terdefinisi'

print(f'faktorial {n}!: {faktorial(n)}')