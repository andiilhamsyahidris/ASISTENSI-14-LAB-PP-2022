# Program Mengonversi Hari ke Tahun, Bulan, dan Hari

x = int(input(''))

def day(x):
    tahun = x // 365
    sisa_tahun = x % 365
    bulan = sisa_tahun // 30
    hari = sisa_tahun % 30

    print(tahun, 'tahun')
    print(bulan, 'bulan')
    print(hari, 'hari')

day(x)