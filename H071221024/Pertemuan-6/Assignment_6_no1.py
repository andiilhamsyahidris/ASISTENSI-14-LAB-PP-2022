try :
    input1=input()
    input2=input()
    with open(f'{input1}.txt', 'r') as file :
        content= file.read()
    with open(f'{input2}.txt', 'x') as file2 :
        file2.write(content)
        print('Berhasil')
except :
    print('Gagal')