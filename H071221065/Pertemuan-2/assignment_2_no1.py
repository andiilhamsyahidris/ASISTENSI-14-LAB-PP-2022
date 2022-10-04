#Mengkonversi  nilai dalam bentuk angka ke huruf

Nilai_= int(input("Masukkan Nilai: "))
if Nilai_>=90: 
    print("Nilai %s = 'A'" % (Nilai_))
elif 80< Nilai_ <=90:
    print("Nilai %s = 'B'" % (Nilai_))
elif 70< Nilai_ <=80:
    print("Nilai %s = 'C'" % (Nilai_))
elif 60< Nilai_ <=70:
    print("Nilai %s = 'D'" % (Nilai_))
elif 40< Nilai_ <=60:
    print("Nilai %s = 'E'" % (Nilai_))
elif Nilai_ <40:
    print("Nilai %s = 'F'" % (Nilai_))