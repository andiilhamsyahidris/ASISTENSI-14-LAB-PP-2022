print("program mencetak angka x horizontal dan y vertikal")
print("            Andi Muthia Mulia Putri               ")
print("==================================================")

x=int(input("Masukkan nilai:"))
y=int(input("Masukkan nilai:"))

for i in range(1,y+1):
     print (i, end=" ")
     if i%x ==0:
          print()