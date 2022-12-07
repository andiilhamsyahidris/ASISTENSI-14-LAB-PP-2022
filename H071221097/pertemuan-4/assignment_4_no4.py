# Menerima sebuah bilangan bulat=>mengembalikan nilai faktorial dari bilangan tersebut

def faktorial(n):
    if n==0:
        return 1
    else:
        return n*faktorial(n-1)

n = int(input())
print (n, " =", faktorial(n)) 