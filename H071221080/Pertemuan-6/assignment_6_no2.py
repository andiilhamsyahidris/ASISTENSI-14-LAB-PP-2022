# Program menyalin file dengan extensi .txt
# kemudian hasil salinannya ditulis kembali format rata kanan

file1 = input('Nama file pertama (auto .txt): ')
file2 = input('Nama file kedua (auto .txt): ')

try:
    with open(file1 + '.txt', 'r') as first_file:
        file1_contents = first_file.readlines()
        longest_line = file1_contents[0]

        for i in file1_contents:
            if len(i) > len(longest_line):
                longest_line = i

                if '\n' not in longest_line:
                    longest_line+= ' '

    with open(file2 + '.txt', 'w') as new_file:
        for j in file1_contents:
            if '\n' in j:
                space = len(longest_line) - len(j)
                new_file.write((' ' * space) + j)
            else:
                different_space = len(longest_line) - len(j) - 1
                new_file.write((' ' * different_space) + j)

    print('\nBerhasil')

except:
    print('\nGagal')