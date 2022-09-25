# program mengonversi angka ke huruf sesuai golongane

x= int(input('Nilai = '))

if x >= 90:
    hasil= 'A'
elif x >= 80:
    hasil= 'B'
elif x >= 70:
    hasil= 'C'
elif x >= 60:
    hasil= 'D'
elif x >= 40:
    hasil= 'E'
elif x < 40:
    hasil= 'F'

print('-> Nilai dari', x, "= '", hasil, "'")