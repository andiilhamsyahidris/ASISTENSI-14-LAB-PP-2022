# Program Menginput Bilangan Bulat Lalu Output Menghasilkan Nilai Faktorial Bilangan Inputan

x = int(input('Nilai n = '))

def faktorial(x):
    if x > 1:
        return x * faktorial(x - 1)
    else:    
        return 1

print(f'{x}! = {faktorial(x)}')