derajat = float(input('derajat: '))
hari = 3600 * 24  
detik = round((derajat/360)*hari)
jam = 6
menit = 0

while(detik >= 3600 ):
    detik -= 3600 
    jam += 1

while(detik >= 60):
    detik -= 60
    menit += 1

jam %= 24

if jam >= 5 and jam <10:
    print("selamat pagi")
elif jam > 10 and jam <= 15:
    print("selamat siang")
elif jam > 15 and jam <= 18:
    print("selamat sore")
elif jam > 18 and jam <= 24:
    print("selamat malam")
else :
    print("selamat malam")

print(f"{jam:02d}:{menit:02d}:{detik:02d}")