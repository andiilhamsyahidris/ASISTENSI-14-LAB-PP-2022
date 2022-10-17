#program detail data diri

print("=" * 60)
print("Selamat datang untuk memulai silahkan input data anda")
print("=" * 60)

nama = input("Masukkan nama : ")
umur = int(input("Masukkan umur : "))
alamat = input("Masukkan alamat : ")

data_diri = {
    "nama": nama, 
    "umur": umur,
    "alamat": alamat 
}

def profil():
    print("=" * 60)
    print('Selamat datang', data_diri.get('nama') ,'silahkan pilih opsi')
    print("=" * 60)
profil()

i = 1
while i > 0 :
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("=" * 60)
    opsi= input("Masukkan opsi : ")
    print("=" * 60)

    try :
        opsi = int(opsi)
    except :
        print("Inputan salah")
    else:
        if opsi==1 :
            print('Data anda adalah')
            print(f"Nama:", data_diri.get('nama'))
            print(f"Umur:", data_diri.get('umur'))
            print(f"Alamat:", data_diri.get('alamat'))
            profil()
        elif opsi==2 :
            nama_baru=input('Silahkan masukkan nama baru: ')
            data_diri['nama'] = nama_baru
            print('Data anda sukses untuk diperbarui')
            profil()
        elif opsi== 3 :
            umur_baru=int(input('Silahkan masukkan umur baru: '))
            data_diri['umur'] = umur_baru
            print('Data anda sukses untuk diperbarui')
            profil()
        elif opsi== 4 :
            alamat_baru=input('Silahkan masukkan alamat baru: ')
            data_diri['alamat'] = alamat_baru
            print('Data anda sukses untuk diperbarui')
            profil()
        elif opsi== 5 :
            print("Selamat tinggal", data_diri.get('nama'))
            break