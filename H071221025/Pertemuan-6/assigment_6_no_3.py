try :
    dataFile=input("masuukkan nama file: ")
    jumlahData=int(input("masukkan jumlah data: "))
    listNama=[]
    listnim=[]
    listAng=[]

    for i in range(jumlahData) :
        nama=input("masukkan nama: ")
        listNama.append(nama)
        nim=input("masukkan nim: ")
        listnim.append(nim)
        angkatan=input("masukkan tahun angkatan: ")
        listAng.append(angkatan)

    longNama = listNama[0]
    for i in listNama :
        if len(i)>len(longNama) :
            longNama=i

    long = len(longNama)

    if long <= 20:
        if len(nim) == 10:
            if len(angkatan) == 4:
                with open(f'{dataFile}.txt','w') as file :
                    file.write('+'+'-'*(len(longNama)+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')
                    file.write('|'+' Nama'+' '*(len(longNama)-3)+'|')
                    file.write(' NIM'+' '*8 +'|')
                    file.write(' Angkatan'+' '*(10-9)+'|\n')
                    file.write('+'+'-'*(len(longNama)+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')

                    for j in range (jumlahData) :
                        longNama = listNama[0]
                        for i in listNama :
                            if len(i)>len(longNama) :
                                longNama=i
                        file.write(f'| {listNama[j]} '+' '*(len(longNama)-len(listNama[j])))
                        file.write(f'| {listnim[j]}'+' '*1)
                        file.write(f'| {listAng[j]}'+' '*5+'|\n')

                    file.write('+'+'-'*(len(longNama)+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')
                    print('Berhasil')
            else :
                print('Gagal')
        else :
            print('Gagal')
    else :
        print('Gagal')
except :
    print('Gagal')