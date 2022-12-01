from assignment_10_no1a import Menu, One, Two, Three
from assignment_10_no1a import Four, Five, Six, Another

# nol = Menu()
satu = One()
dua = Two()
tiga = Three()
empat = Four()
lima = Five()
enam = Six()
beda = Another()

while True:
    Menu.decoration(75)
    Menu.opsi_list()
    opsi = input('Silahkan Pilih Opsi Anda : ')
    if opsi == '1':
        satu.pilihan()
    elif opsi == '2':
        dua.pilihan()
    elif opsi == '3':
        tiga.pilihan()
    elif opsi == '4':
        empat.pilihan()
    elif opsi == '5':
        lima.pilihan()
    elif opsi == '6':
        enam.pilihan()
        break
    else:
        beda.pilihan()
        