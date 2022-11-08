# Membuat class berdasarkan class diagram

class Kubus :
    def __init__(self, lebar, tinggi, panjang) :
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang 

    def setMassa(self, massa) :
        self.massa = massa 
    def getMassaJenis (self) :
        self.volume = self.panjang * self.lebar * self.tinggi 
        self.MassaJenis = self.massa / self.volume
        return self.MassaJenis

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

objKubus = Kubus(lebar, tinggi, panjang)
objKubus.setMassa(massa)
print ('massa jenis = ', objKubus.getMassaJenis())

objKubus.setMassa(massa*2)
print ('massa jenis : ' , objKubus.getMassaJenis())