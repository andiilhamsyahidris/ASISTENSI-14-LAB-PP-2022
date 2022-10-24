try :
    filename=input()
    range1=int(input())
    listname=[]
    listnim=[]
    listyear=[]

    for x in range(range1) :
        name=input()
        listname.append(name)
        nim=input()
        listnim.append(nim)
        year=input()
        listyear.append(year)

    longName = listname[0]
    for a in listname :
        if len(a)>len(longName) :
            longName=a
    x=len(longName)

    if x<=20:
        if len(nim)==10:
            if len(year)==4:
                with open(f'{filename}.txt','x') as file :
                    file.write('+'+'-'*(len(longName)+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')
                    file.write('|'+' Nama'+' '*(len(longName)-5+2)+'|')
                    file.write(' NIM'+' '*(10-4+2)+'|')
                    file.write(' Angkatan'+' '*(10-9)+'|\n')
                    file.write('+'+'-'*(len(longName)+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')

                    for j in range (range1) :
                        longName = listname[0]
                        for i in listname :
                            if len(i)>len(longName) :
                                longName=i
                        file.write(f'| {listname[j]} '+' '*(len(longName)-len(listname[j])))
                        file.write(f'| {listnim[j]}'+' '*1)
                        file.write(f'| {listyear[j]}'+' '*5+'|\n')

                    file.write('+'+'-'*(len(longName)+2)+'+')
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