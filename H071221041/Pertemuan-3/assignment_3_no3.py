harga  = int(input("Harga barang:"))
uang= int(input("Nilai uang:"))

if harga<=uang:
    kembalian=(uang-harga)

    d=[100000,50000,20000,10000,5000,2000,1000,500,200,100]
    for i in d:
        pembagian_kembalian=kembalian//i
        print(f"{int(pembagian_kembalian)} uang Rp.{i}")
        kembalian=kembalian-(pembagian_kembalian*i)

else:print("uang nda cukup")
