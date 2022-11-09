class kubus :
    def __init__ (kubus, setLebar, setTinggi, setPanjang) :
        kubus.setLebar = float(setLebar)
        kubus.setTinggi = float(setTinggi)
        kubus.setPanjang = float(setPanjang)
    def setMassa (kubus, setMassa) :
        kubus.massa = float(setMassa)
    def getMassaJenis(kubus) :
        return kubus.massa/(kubus.setLebar*kubus.setTinggi*kubus.setPanjang)

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = kubus(lebar, tinggi, panjang)

kubus.setMassa(massa)
print ("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print ("Massa Jenis =", kubus.getMassaJenis())

