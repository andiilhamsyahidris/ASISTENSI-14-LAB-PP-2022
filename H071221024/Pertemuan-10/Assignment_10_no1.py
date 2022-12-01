from Data import Person
import re
import os
a=0
b=0
c=0
d=0
while True :
    def equals(a) :
        for i in range(a) :
            print('=', end='')

    equals(100)
    print(f'\nSelamat datang silahkan pilih opsi menu anda')
    print('1. Detail anda')
    print('2. Ubah Nama')
    print('3. Jumlah Data pada File')
    print('4. Save Data pada File')
    print('5. Buat Data Baru')
    print('6. Keluar')

    try :
        option=int(input('Silahkan Pilih Opsi Anda: '))
        equals(100)

        if option==1 :
            if a==0 :
                print('\nData Saat Ini Kosong')
            elif a>0 :
                print('\nData Anda Adalah')
                print('Nama: ', person.GetName() )
                print('Email: ', person.GetEmail() )
                print('Password: ', person.GetPassword())
        elif option==2 :
            if a == 0 :
                print('\nData saat ini kosong')
            if a > 0 :
                newName=input('\nMasukkan nama baru: ')
                person.SetName(newName)
        elif option==3 :
            inpFile=input('\nSilahkan Masukkan Nama File: ')
            if os.path.exists(f'{inpFile}.txt') :
                print(f'Jumlah Data pada file: {b} Data')
            else :
                print(f'Tidak terdapat file dengan nama {inpFile}.txt')
                print(f'Jumlah Data pada file: 0 Data')
        elif option==4 :
            if a == 0 :
                print('\nData Saat Ini Kosong')
            elif a > 0 :
                saveFile=input('\nInput nama file yang akan disimpan: ')
                with open (f'{saveFile}.txt','a') as file :
                    if c==0 : 
                        file.write('+'+'='*99)
                        file.write('\n|'+'Data yang tersimpan\n')
                        file.write('+'+'='*99+' \n')
                        file.write('|'+'Nama'+' '*12+': ' + person.GetName())
                        file.write('\n|'+'Email'+' '*11+': ' + person.GetEmail())
                        file.write('\n|'+'Password'+' '*8+': ' + person.GetPassword())
                        file.write('\n+'+'='*99)
                        a=0
                        b+=1
                        c+=1
                        print('Berhasil')
                    elif c > 0 :
                        file.write('\n|'+'Nama'+' '*12+': ' + person.GetName())
                        file.write('\n|'+'Email'+' '*11+': ' + person.GetEmail())
                        file.write('\n|'+'Password'+' '*8+': ' + person.GetPassword())
                        file.write('\n+'+'='*99)
                        a=0
                        b+=1
                        print('Berhasil')
        elif option==5 :
            d-=1
            inpName=input('\nSilahkan Masukkan Nama Anda: ')
            while d<0 :
                inpEmail=input('Silahkan Masukkan Email Anda: ')
                match=re.findall(r'^[a-z]+[0-9]+@student[.]unhas[.]ac[.]id$', inpEmail)
                if match :
                    while d<0 :
                        inpPass=input('Silahkan Masukkan Password Anda: ')
                        if len(inpPass) >=8 and len(inpPass) <=20 :
                            match2=re.findall(
                                r'[!@#$%^&*+=]?[A-Z]+[!@#$%^&*+=]?[a-z]+[!@#$%^&*+=]?[0-9]+[!@#$%^&*+=]?|[!@#$%^&*+=]?[a-z]+[!@#$%^&*+=]?[A-Z]+[!@#$%^&*+=]?[0-9]+[!@#$%^&*+=]?|[!@#$%^&*+=]?[A-Z]+[!@#$%^&*+=]?[0-9]+[!@#$%^&*+=]?[a-z]+[!@#$%^&*+=]?|[!@#$%^&*+=]?[a-z]+[!@#$%^&*+=]?[0-9]+[!@#$%^&*+=]?[A-Z]+[!@#$%^&*+=]?|[!@#$%^&*+=]?[0-9]+[!@#$%^&*+=]?[a-z]+[!@#$%^&*+=]?[A-Z]+[!@#$%^&*+=]?|[!@#$%^&*+=]?[0-9]+[!@#$%^&*+=]?[A-Z]+[!@#$%^&*+=]?[a-z]+[!@#$%^&*+=]?', inpPass)
                            if match2 :
                                a+=1
                                d+=1
                                person=Person(inpName,inpEmail,inpPass)
                            else :
                                equals(100)
                                print('\nPassword yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka')
                                print('='*100)
                        else :
                            equals(100)
                            print('\nPassword harus memiliki Panjang 8-20 karakter')
                            print('='*100)
                else :
                    equals(100)
                    print('\nEmail yang Anda Masukkan Salah')
                    print('='*100)
        elif option==6 :
            print(f'\nSampai Jumpa Lagi')
            break
        else :
            print('\nInputan harus berupa angka 1-6')
    except :
        equals(100)
        print('\nInputan harus berupa angka 1-6')