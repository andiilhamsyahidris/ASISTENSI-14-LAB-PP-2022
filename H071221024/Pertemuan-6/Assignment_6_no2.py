try :
    input1=input()
    input2=input()
    listline=[]
    with open(f'{input1}.txt', 'r') as file :
        for x in file :
            x=x.replace('\n','')
            listline.append(x)
    with open(f'{input2}.txt', 'x') as file2 :
        for j in range (len(listline)) :
            longLine = listline[0]
            for i in listline :
                if len(i)>len(longLine) :
                    longLine=i
            file2.write(' '*(len(longLine)-len(listline[j]))+f'{listline[j]}\n')
        print('Berhasil')
except :
    print('Gagal')