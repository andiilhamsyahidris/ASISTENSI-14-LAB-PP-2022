x = int(input("masukkan nilai total belanja:Rp. "))
y = int(input("masukkan nilai uang yang dibayar:Rp. "))

if x <= y:
    z = y - x

    n = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

    for i in n:
        pembagian_kembalian = z//i
        print(f"{int(pembagian_kembalian)} uang Rp. {i}")
        z = z - (pembagian_kembalian*i)  

else:
    print("uang tidak cukup")