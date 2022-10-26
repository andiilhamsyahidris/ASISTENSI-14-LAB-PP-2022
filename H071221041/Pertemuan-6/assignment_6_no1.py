file = input("masukkan nama file: ")
file2 = input("masukkan nama file2: ")

try:
    with open(file + ".txt", "r") as file:
        data = file.read()
        file.closed

    with open(file2 + ".txt", "a") as file2:
            if (data != -1):
                file2.write(data)
                file2.closed
    print("Berhasil")
except:
    print("Gagal")