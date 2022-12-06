from abc import ABC, abstractmethod

class Motor(ABC): # Inheritance (Kelas Parents)
    def __init__(self, nama, jenis):
        self._nama = nama   # Encapsulation
        self._jenis = jenis # Encapsulation
    @abstractmethod # kelas Abstrak
    def getName (self) :
        pass
    @abstractmethod
    def getJenis (self) :
        pass

class Sport(Motor): # Inheritance (Kelas Child)
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)
    def getName (self) :
        return self._nama
    def getJenis (self) :
        return self._jenis
    def komen(self):
        print("Motor jenis ini dapat melaju hingga 300 km/jam ")
        print("Contoh motor jenis ini : CBR, Ninja H2R, Ninja ZX25R, R1, dan Panigale V4 ")

class Metic(Motor): # Inheritance (Kelas Child)
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)
    def getName (self) :
        return self._nama
    def getJenis (self) :
        return self._jenis
    def komen(self):
        print("Motor jenis ini adalah motor yang paling mudah untuk dikendarai ")
        print("Contoh motor jenis ini : Beat, Mio, N-Max, ADV, X-Max, Forza, dan X-ADV 160")

class Trail(Motor): # Inheritance (Kelas Child)
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)
    def getName (self) :
        return self._nama
    def getJenis (self) :
        return self._jenis
    def komen(self):
        print("Motor jenis ini dapat digunakan pada medan off road ")
        print("Contoh motor jenis ini : KLX, CRF 150, WR 155, dan CBR 1100L Africa Twin")

class Bebek(Motor): # Inheritance (Kelas Child)
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)
    def getName (self) :
        return self._nama
    def getJenis (self) :
        return self._jenis
    def komen(self):
        print("Motor jenis ini adalah motor yang irit bahan bakar ")
        print("Contoh motor jenis ini : Jupiter Z, Smash, dan Supra Bapak")


#Polymorfhism
def komentar(motor) :
    motor.komen()


# Objek
supra = Bebek("supra", "bebek")
cbr   = Sport("cbr", "sport")

print ("Nama Motor :", supra.getName())
print ("Jenis      :", supra.getJenis())
komentar(supra)
print("-"*80)
print ("Nama Motor :", cbr.getName())
print ("Jenis      :", cbr.getJenis())
komentar(cbr)