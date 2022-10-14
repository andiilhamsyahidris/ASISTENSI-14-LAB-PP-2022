# Program mengubah detail data

print('===============================================================')
print('Selamat datang! Untuk memulai, silahkan input data anda!')
print('===============================================================')

nama = input('Input nama: ')
umur = int(input('Input umur: '))
alamat = input('Input alamat: ')

profile = {
    'Nama': nama,
    'Umur': umur,
    'Alamat': alamat
}

while True:
    print('===============================================================')
    print(f'Selamat datang {nama}, silahkan pilih opsi')
    print('===============================================================')
    print('1. Detail anda')
    print('2. Ubah Nama')
    print('3. Ubah Umur')
    print('4. Ubah Alamat')
    print('5. Keluar')
    print('===============================================================')
    opsi = int(input('Input opsi: '))
    print('===============================================================')
    if opsi == 1:
        print('Data anda adalah')
        print('Nama:',profile['Nama'])
        print('Umur:',profile['Umur'])
        print('Alamat:',profile['Alamat'])
    elif opsi == 2:
        nama = input('Silahkan input data nama baru: ')
        profile['Nama'] = nama
        print('Data anda sukses diperbaharui')
    elif opsi == 3:
        umur = int(input('Silahkan input data umur baru: '))
        profile['Umur'] = umur
        print('Data anda sukses diperbaharui')
    elif opsi == 4:
        alamat = input('Silahkan input data alamat baru: ')
        profile['Alamat'] = alamat
        print('Data anda sukses diperbaharui')
    elif opsi == 5:
        print(f'Selamat tinggal {nama}')
        break
    else:
        print('Opsi salah, masukkan ulang opsi yang benar!')