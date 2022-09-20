# menghitung total gaji

a= input('Nama : ')
b= float(input('Gaji pokok : '))
c= float(input('Total penjualan : '))

total1= c * 15/100
total2= total1 + b
total3= round(total2, 2)

print('TOTAL = $', total3)