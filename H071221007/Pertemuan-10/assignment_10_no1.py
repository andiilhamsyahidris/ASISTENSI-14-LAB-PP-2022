import re
import os  
from data import Person

tersimpan = 0
banyakdata = 0

while True:
    a = 0
    print(50*'=')
    print('Selamat Datang Silahkan Pilih Opsi Menu Anda')
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Jumlah data pada file")
    print("4. Save data pada file")
    print("5. Buat data Baru") 
    print("6. Keluar")
    opsi = input("silahkan pilih opsi anda : ")

    if opsi == '1':
        if banyakdata == 0:
            print(50*'=')
            print("Data saat ini kosong")
        else:
            print(50*'=')
            print("Data anda adalah")
            print("Nama     :", orang.getname())
            print("Email    :", orang.getemail())
            print("Password :", orang.getpassword())

    elif opsi == '2':
        if banyakdata == 0:
            print(50*'=')
            print("Data saat ini kosong")
        else:
            print(50*'=')
            newName = input("Silahkan input nama baru : ")
            orang.setname(newName)

    elif opsi == '3':
        print(50*'=')
        fileName = input("Silahkan masukkan nama file : ")
        if os.path.exists(f"{fileName}.txt"):
            print(f"Jumlah data anda adalah : {tersimpan} data")
        else:
            print(f"tidak terdapat file dengan nama {fileName}.txt")
            print(f"Jumlah data anda adalah : 0 data")

    elif opsi == '4':
        if banyakdata == 0:
            print(50*'=')
            print("Data saat ini kosong")
        else:
            print(50*'=')
            namafile = input("Masukkan Nama file baru anda : ")
            with open (f'{namafile}.txt','a') as file :
                if tersimpan == 0 :
                    file.write(f"+{'='*100}\n")
                    file.write(f"|Data yang tersimpan\n")
                    file.write(f"+{'='*100}\n")
                    file.write(f"|Nama     : {orang.getname()}\n")
                    file.write(f"|Email    : {orang.getemail()}\n")
                    file.write(f"|Password : {orang.getpassword()}\n")
                    file.write(f"+{'='*100}\n")
                    tersimpan += 1
                elif tersimpan > 0 :
                    file.write(f"|Nama     : {orang.getname()}\n")
                    file.write(f"|Email    : {orang.getemail()}\n")
                    file.write(f"|Password : {orang.getpassword()}\n")
                    file.write(f"+{'='*100}\n")
                    print("Berhasil")
                    tersimpan += 1

    elif opsi == '5':
        print(50*'=')
        a += 1
        nama = input("Silahkan Masukkan Nama Anda : ")
        while a > 0 :
            email = input("Silahkan masukkan email anda : ")
            match = re.findall(r"^[a-z0-9]+\@student\.unhas\.ac\.id$", email)
            if match :
                while a > 0 :
                    password = input('Silahkan masukkan password anda : ')
                    if len(password) >= 8 and len(password) <= 20 :
                        match2 = re.findall(f"[A-Z]+", (password)) and re.findall(f"[a-z]+", (password)) and re.findall("[0-9]+", (password))
                        if match2 :
                            orang = Person(nama, email, password)
                            a -= 1
                            banyakdata += 1
                        else :
                            print(50*'=')
                            print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
                            print(50*'=')
                    else : 
                        print(50*'=')
                        print("Password harus memiliki 8-20 karakter")
                        print(50*'=')
            else:
                print(50*'=')  
                print("Email yang anda masukkan salah")
                print(50*'=')

    elif opsi == '6':
        print('Sampai jumpa lagi')
        break 
    else :
        print(50*'=')
        print('Silahkan pilih opsi 1 sampai 6')