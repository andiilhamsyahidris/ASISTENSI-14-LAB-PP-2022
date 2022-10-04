#

price = int(input('Harga barang : '))
pay = int(input('Nilai uang : '))

if price <= pay:
    change = pay - price
    
    money_list = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    
    for i in money_list:
        money = change // i
        print(f'{money} uang Rp. {i}')
        change = change - (money * i)

else:
    print('Uang tidak cukup')