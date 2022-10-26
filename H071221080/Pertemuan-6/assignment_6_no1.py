# Program menyalin file dengan extenxi .txt

file1 = input('Nama file pertama (auto .txt): ')
file2 = input('Nama file kedua (auto .txt): ')

try: 
    with open(file1 + '.txt', 'r') as first_file:
        file1_contents = first_file.read()
        
    with open(file2 + '.txt', 'x') as new_file:
        new_file.write(file1_contents)

    print('\nBerhasil')

except:
    print('\nGagal')

# with open('Latihan.txt', 'w') as file:
#     file.write('Baris pertama')
#     file.write('\nBaris kedua')
#     file.write('\nBaris ketiga')

        # if file1 != None:
        # else:
        #     print('Gagal')