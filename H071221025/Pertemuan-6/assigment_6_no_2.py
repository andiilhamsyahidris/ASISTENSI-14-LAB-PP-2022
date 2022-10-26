file = input("masukkan nama file: ")
file2 = input("masukkan nama file2: ")

try:
    with open(file + ".txt", "r") as file:
        data = file.readlines()
        print(data)

        data[2] = data[2]+"\n"

        x = 0
        for i in data:
            if len(i) > x:
                x = len(i)

    with open(file2 + ".txt", "w") as file2:
        for i in data:
            file2.write(i.rjust(x))
            
    print("Berhasil")

except:
    print("Gagal")