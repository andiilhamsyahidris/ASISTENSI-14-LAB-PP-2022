hargaBarang=int(input('Masukkan nilai harga barang: '))
nilaiUangYangDibayar=int(input('Masukkan Nilai uang yang dibayar: '))

uangKembalian=nilaiUangYangDibayar-hargaBarang

uang100=uangKembalian//100000
sisa1=uangKembalian-(uang100*100000)
uang50=sisa1//50000
sisa2=sisa1-(uang50*50000)
uang20=sisa2//20000
sisa3=sisa2-(uang20*20000)
uang10=sisa3//10000
sisa4=sisa3-(uang10*10000)
uang5=sisa4//5000
sisa5=sisa4-(uang5*5000)
uang2=sisa5//2000
sisa6=sisa5-(uang2*2000)
uang1=sisa6//1000

daftarUang=[100000,50000,20000,10000,5000,2000,1000]

for k in daftarUang :
    uang100 = (uangKembalian//k)
    uangKembalian=uangKembalian%k
    print(f'{uang100} uang Rp. {k}')