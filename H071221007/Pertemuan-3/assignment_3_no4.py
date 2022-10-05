baris = int(input("Masukkan jumlah baris :"))

for i in range (1,baris+1):
    b = (baris-i)*'  '
    c = (i * " *") 
    d = ((i-1) * " *")
    print (b+c+d) 