def getFPB(x,y):
    if x<y :
        terkecil=y
    else :
        terkecil=x
    for i in range (1,terkecil+1) :
        if x%i==0 and y%i==0:
            fpb=i
    return fpb
bilangan1=int(input('Masukkan Bilangan ke-1: '))
bilangan2=int(input('Masukkan Bilangan ke-2: '))
print(f'FPB({bilangan1},{bilangan2})= {getFPB(bilangan1,bilangan2)}')