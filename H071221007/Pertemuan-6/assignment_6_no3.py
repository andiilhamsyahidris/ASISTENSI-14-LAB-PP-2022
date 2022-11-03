nama_file = input("Masukkan nama file: ")+'.txt' 
n = int(input("Masukkan jumlah data :"))
list_nama = []
list_nim = []
list_angkatan = []

#try :
for i in range (n):
  nama = input("Nama : ")
  list_nama.append (nama)
  nim = input ("NIM : ")
  list_nim.append (nim)
  angkatan = input("Angkatan : ")
  list_angkatan.append (angkatan)

terpanjang = len(list_nama[0])
for j in list_nama :
  if len(j) > terpanjang :
    terpanjang = len(j)

with open (nama_file,'w') as file :
  if len(nama) < 20 :
    file.write ('+'+('-'*(terpanjang+2))+ '+' + ('-'*12)+ '+' + ('-'*10)+'+\n')
    file.write ('| '+'Nama'+(' '*((terpanjang-5)+2))+ '| ' + 'NIM' + (' '*8)+ '| ' + 'Angkatan' + ' |\n')
    file.write ('+'+('-'*(terpanjang+2))+ '+' + ('-'*12)+ '+' + ('-'*10)+'+\n')
    for i in range (n) :
      file.write ('| ' + f'{list_nama[i]}' + (' '*(terpanjang-len(list_nama[i])+1)))
      file.write ('| ' + f'{list_nim[i]}' + ' ')
      file.write ('| ' + f'{list_angkatan[i]}' + (' '*5) + '|\n')
    print('\nBerhasil')
  else : 
    print('\nGagal')

#except :
  #print('\nGagal') 