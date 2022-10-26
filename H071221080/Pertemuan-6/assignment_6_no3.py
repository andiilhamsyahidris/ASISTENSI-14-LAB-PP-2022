# Program menyalin nama, NIM, dan angkatan
# semua asisten Pengantar Pemrograman

try:
    file_name = input('Nama file: ')
    data_amount = int(input('Jumlah data yang akan diinput: '))

    name = []
    NIM = []
    college_year = []

    for i in range(data_amount):
        name_contents = input(f'Nama ke-{i+1}: ')
        name_contents = name_contents.replace(' ', '_')
        name.append(name_contents)

        isi_NIM = input(f'NIM orang ke-{i+1}: ')
        NIM.append(isi_NIM)

        year_contents = int(input(f'Angkatan orang ke-{i+1}: '))
        year_contents = str(year_contents)
        college_year.append(year_contents)

    for j in name:
        if len(j) > 20:
            print('\nGagal')
            break

    else:
        with open(file_name + '.txt', 'w') as file:
            longest_name = name[0]
            
            for name_range in name:
                if len(name_range) > len(longest_name):
                    longest_name = name_range

            file.write('+-' + ('-' * len(longest_name)) + '-+')
            file.write(('-' * 12) + '+')
            file.write(('-' * 10) + '+')

            file.write('\n| Nama' + (' ' * (len(longest_name) - 5)) + '  |')
            file.write(' NIM' + (' ' * (12 - 4)) + '|')
            file.write(' Angkatan' + (' ' * (10 - 9)) + '|')

            file.write('\n+-' + ('-' * len(longest_name)) + '-+')
            file.write(('-' * 12) + '+')
            file.write(('-' * 10) + '+')

            for x in range(data_amount):
                file.write('\n| ')
                file.write(name[x])
                file.write(' ' * (len(longest_name) - len(name[x])) + ' | ')
                file.write(NIM[x])
                file.write(' ' * (11 - len(NIM[x])) + '| ')
                file.write(college_year[x])
                file.write((' ' * (9 - len(college_year[x]))) + '|')

            file.write('\n+-' + ('-' * len(longest_name)) + '-+')
            file.write(('-' * 12) + '+')
            file.write(('-' * 10) + '+')

        print('\nBerhasil')

except:
    print('\nGagal\n-> Ada kesalahan inputan')