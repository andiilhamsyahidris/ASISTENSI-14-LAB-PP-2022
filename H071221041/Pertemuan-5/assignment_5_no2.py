print("Selamat datang untuk memulai silahkan input data anda")

nama = input("Input Nama : ")
umur = int(input("Input Umur : "))
alamat = input("Input Alamat : ")

dataDiri = {
"Nama": nama, 
"Umur": umur,
"Alamat": alamat 
}

def profil():
    print("=" * 60)
    print('Selamat datang', dataDiri.get('Nama') ,'silahkan pilih opsi')
    print("========================================================")
profil()

i = 1
while i > 0 :
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("=" * 60)
    a= input("Input opsi : ")
    print("=" * 60)

    try :
        a = int(a)
    except :
        print("Inputan salah")
    else:
        if a == 1:
            print("Data anda adalah")
            print('Nama :', dataDiri.get('Nama'))
            print('Umur :', dataDiri.get('Umur'))
            print('Alamat :', dataDiri.get('Alamat'))
            profil()
        elif a == 2:
            nama_baru = input("Silahkan input nama baru : ")
            dataDiri['Nama'] = nama_baru
            print("Data anda sukses di perbarui")
            profil()
        elif a == 3:
            umur_baru = input("Silahkan input umur baru : ")
            dataDiri['Umur'] = umur_baru
            print("Data anda sukses di perbarui")
            profil()
        elif a == 4:
            alamat_baru = input("Silahkan input alamat baru : ")
            dataDiri['Alamat'] = alamat_baru
            print("Data anda sukses di perbarui")
            profil()
        elif a == 5:
            print('Selamat Tinggal', dataDiri.get('Nama'))
            break