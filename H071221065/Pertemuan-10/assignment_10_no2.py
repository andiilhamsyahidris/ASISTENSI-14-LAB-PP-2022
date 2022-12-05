class Kendaraan:
    def __init__(self, merek, roda):
        self.brand = merek
        self.wheel = roda

    def setBrand(self, merek):
        self.brand = merek

    def getBrand(self):
        return self.brand

    def setWheel(self, roda):
        self.wheel = roda

    def getWheel(self):
        return self.wheel

    def remMendadak(self):
        self._speed = 0


class Motor(Kendaraan):
    def __init__(self, merek, roda):
        super().__init__(merek, roda)
        self._speed = 140
        self._weight = 80
        self._price = 16000
        self.__pasengger = 2

    def gasspol(self):
        self._speed = self._speed+60

    def setSpeed(self, kecepatan):
        self._speed = kecepatan

    def getSpeed(self):
        return self._speed

    def setWeight(self, berat):
        self._weight = berat

    def getWeight(self):
        return self._weight

    def setPenumpang(self, penumpang):
        self.__pasengger = penumpang

    def getPenumpang(self):
        return self.__pasengger

    def setHarga(self, harga):
        self._price = harga

    def getHarga(self):
        return self._price


class Mobil(Kendaraan):
    def __init__(self, merek, roda):
        super().__init__(merek, roda)
        self._speed = 500
        self._weight = 300
        self._price = 200000
        self._pasengger = 5

    def gasspol(self):
        self._speed = self._speed+120

    def setSpeed(self, kecepatan):
        self._speed = kecepatan

    def getSpeed(self):
        return self._speed

    def setWeight(self, berat):
        self._weight = berat

    def getWeight(self):
        return self._weight

    def setPenumpang(self, penumpang):
        self._pasengger = penumpang

    def getPenumpang(self):
        return self._pasengger

    def setHarga(self, harga):
        self._price = harga

    def getHarga(self):
        return self._price


class Matic(Motor):
    def __init__(self, merek, roda):
        super().__init__(merek, roda)
        self._price = 20000

    def special(self):
        print(f'{self.brand}tidak perlu ganti gigi')


class Manual(Motor):
    def __init__(self, merek, roda):
        super().__init__(merek, roda)
        self._weight = 60

    def special(self):
        self._speed = self._speed+20
        print(f'{self.brand} perlu ganti gigi tapi kecepatan bertambah 20 tiap ganti gigi menjadi {self._speed}')


class DuaKabin(Mobil):
    def __init__(self, merek, roda):
        super().__init__(merek, roda)
        self._price = 210000
        self._speed = 600

    def special(self):
        print(f"Bisa Sat Set Sat Set waktu macet")


class TigaKabin(Mobil):
    def __init__(self, merek, roda):
        super().__init__(merek, roda)
        self._price = 300000

    def special(self):
        self._pasengger = self._pasengger+3


class Jual_Kendaraan:
    def kondisiendaraan(self):
        pass


class Bekas(Jual_Kendaraan):
    def __init__(self) -> None:
        super().__init__()
        self._price = "Murah"


class Baru(Jual_Kendaraan):
    def __init__(self) -> None:
        super().__init__()
        self._price = "Mahal"


Toyota = TigaKabin("Toyota", roda=4)
Toyota.gasspol()
Toyota.special()
print(f"kecepatan mobil toyota adalah : {Toyota.getSpeed()}")
print(f"Toyota dapat menampung {Toyota.getPenumpang()} penumpang")
print(f"harga mobil Toyota adalah {Toyota.getHarga()}000 rupiah")
