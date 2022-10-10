x=int(input('Masukkan Usia Dalam Hari: '))

def myDay(x):
    tahun= int(x//365)
    bulan= int(x%365//30)
    hari= int(x-(tahun*365)-(bulan*30))
    bulan%=12
    print(f'{tahun} tahun')
    print(f'{bulan} bulan')
    print(f'{hari} hari')
myDay(x)