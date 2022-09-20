# program merubah detik ke dalam format jam:menit:detik

x= int(input('Total detik : '))

a= x // 3600
b1= x % 3600
b2= b1 // 60
c= b1 % 60

print(a, 'jam :', b2, 'menit :', c, "detik")