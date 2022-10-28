# Menyalin file. kemudian hasil salinananya ditulis kembali dengan format rata kanan

try:
    nama_file = input('Masukkan nama file : ') + '.txt'
    salinan = input('Masukkan nama file salinan : ') + '.txt'
    check_len= 0 
  
    listname = []
    with open (nama_file, "r") as fileasli :
        for x in fileasli:
            x = x.replace('\n', '')
            listname.append(x)
        
    with open (salinan, "w") as filecopy:
        for i in range (len(listname)):
            check_len = len(listname[0])
            for j in listname:
                if len(j) > check_len:
                    check_len = len(j)
                    
            filecopy.write(' ' * (check_len - len(listname[i])) + f'{listname[i]}\n')
        print('berhasil')
        
except:
    print('Gagal')