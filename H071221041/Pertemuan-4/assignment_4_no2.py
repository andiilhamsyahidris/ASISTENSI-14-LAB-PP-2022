print("Andi Muthia Mulia Putri")
print('=======================')
x = int(input("masukkan nilai bilangan: "))

def isPrime(x):
    if(x <= 1):
        return False
    for i in range(2,x):
        if (x % i == 0):
            return False
    return True

if isPrime(x):
    print("ini bilangan prima")
else:
    print("ini bukan bilangan prima")