# Membuat class yang menerapkan konsep encapsulation,
# class abstract, inheritance, dan polymorphis

from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, atribut):
        self._name = name
        self._atribut = atribut
        self._health = 5000
        self._power = 200
        self._defense = 2000
        
    def setAtribut(self):
        if self._atribut == 'Panci Emak':
            self._defense +=  500
        elif self._atribut == 'Milo Energen':
            self._health += 700
        elif self._atribut == 'Kopi Toraja':
            self._power += 500
            self._health -= 1000
        elif self._atribut == 'Sapu Ibu':
            self._power += 350
            self._defense -= 350
        elif self._atribut == 'Rim Besi':
            self._power += 150
        elif self._atribut == 'Es Kepal Milo':
            self._defense += 1000
            self._power -= 50
            
    def getName(self):
        return self._name
    
    def getAttribut(self):
        return self._atribut
    
    def getHealth(self):
        return self._health
    
    def getPower(self):
        return self._power
    
    def getDefense(self):
        if self._defense < 0:
            return 0
        else:
            return self._defense
    
    def getClass(self):
        return self._class
            
    def skill1(self, target):
        if target._defense > 0:
            kondisi1 = self._power * (50/100)
            target._defense -= kondisi1
            kondisi2 = self._power * (15/100)
            target._health -= kondisi2
        else:
            self._health += 100
            kondisi2 = self._power * (50/100)
            target._health -= kondisi2
            
    def skill2(self, target):
        kondisi1 = self._power * (25/100)
        target._health -= kondisi1
        
    @abstractmethod
    def ultimate(self):
        pass
    
    @abstractmethod
    def voice1(self):
        pass
    
    @abstractmethod
    def voice2(self):
        pass
        
class Petarunk(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'Petarunk'
        self._health = 3500
        self._power = 500
        self._defense = 1500
        
    def ultimate(self, target):
        target._health -= self._power
        kondisi1 = target._defense * (25/100)
        target._defense -= kondisi1
        print('--- Ultimate Petarunk akan mengabaikan defense target ')
        print('dan langsung menembus ke health target')
        print('skaligus menghancurkan 25% defense targetnya ---\n')
        print(f'{self._name} : "Rasakan blade of hunter blood ini!"')
        
    def voice1(self):
        print(f'{self._name} : "Aku berjiwa petarunk dan aku suka bertarunk, gelud dek?"')
        
    def voice2(self):
        print(f'{self._name} : "Pedangku sudah haus akan darah"')
        
class Dukun(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'Dukun'
        self._health = 3700
        self._power = 400
        self._defense = 1700
    
    def ultimate(self, target):
        target._defense -= target._defense * (60/100)
        target._health -= target._health * (25/100)
        print('--- Ultimate Dukun akan menghancurkan 60% defense')
        print('dan 25% darah target ---\n')
        print(f'{self._name} : "Rasakan kehancuran ini!"')
        
    def voice1(self):
        print(f'{self._name} : "Cabul atau ditipu?"')
        
    def voice2(self):
        print(f'{self._name} : "Obat ini akan bercampur dengan kekuatan skill"')
                
class WadimorBoy(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'Wadimor Boy'
        self._power = 250
        
    def ultimate(self, target):
        self._power *= 1.5
        if target._defense > 0:
            kondisi1 = self._power * (75/100)
            target._defense -= kondisi1
            kondisi2 = self._power * (25/100)
            target._health -= kondisi2
        else:
            target._health -= self._power
        print('--- Ultimate Wadimor Boy akan menyerang target')
        print('dengan power sebesar 150% ---\n')
        print(f'{self._name} : "Jangan remehkan wadimorku, rasakan kekuatan sarung kebanggaan ini"')
        
    def voice1(self):
        print(f'{self._name} : "Wadimor nih bos"')
        
    def voice2(self):
        print(f'{self._name} : "Wadimor siap, waktunya kita tabok musuh"')

class CobuzierMan(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'Cobuzier Man'
        self._health = 7000
        self._defense = 3300
        
    def ultimate(self, target):
        self._health += 500
        self._power += 100
        if target._defense > 0:
            kondisi1 = self._power * (75/100)
            target._defense -= kondisi1
            kondisi2 = self._power * (25/100)
            target._health -= kondisi2
        else:
            target._health -= self._power
        print('--- Ultimate Cobuzier Man akan menambah darahnya')
        print('sendiri dan langsung menyerang targetnya ---\n')
        print(f'{self._name} : "AKU KARAKTER TERKUAT, sini kuhantam kau"')
        
    def voice1(self):
        print(f'{self._name} : "Aku karakter dengan health terbanyak bos, ada lawan?"')
        
    def voice2(self):
        print(f'{self._name} : "Sekali kutumbuk, geprek dia"')

class BocilLatto(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'Bocil Latto'
        self._health = 4000
        self._defense = 3000
    
    def ultimate(self, target):
        kondisi1 = (50/100) * self._defense
        self._power += kondisi1
        self._defense -= kondisi1
        if target._defense > 0:
            kondisi2 = self._power * (75/100)
            target._defense -= kondisi2
            kondisi3 = self._power * (25/100)
            target._health -= kondisi3
        else:
            target._health -= self._power
        print('--- Ultimate Bocil Latto akan mengonversi 50% darahnya')
        print('menjadi power dan akan menyerang target')
        print('dengan power yang sudah ditingkatkan ---\n')
        print(f'{self._name} : "Latto-lattokku akan membuatmu benjol"')
        
    def voice1(self):
        print(f'{self._name} : "Apa? Kamu risih mendengarkan latto-lattokku?"')
        
    def voice2(self):
        print(f'{self._name} : "Latto-latto siap, waktunya cari masalah"')
    
class OrangDepresi(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'Orang Depresi'
        self._health = 2500
        self._power = 900
        self._defense = 750
        
    def ultimate(self, target):
        self._power *= 2
        if target._defense > 0:
            kondisi1 = self._power * (75/100)
            target._defense -= kondisi1
            kondisi2 = self._power * (75/100)
            target._health -= kondisi2
        else:
            target._health -= self._power
        print('--- Ultimate Orang Depresi akan melipatgandakan powernya')
        print('dan akan menyerang darah dan defense target')
        print('sebesar 75% powernya ---\n')
        print(f'{self._name} : "BERHENTI MENGGANGGUKU!!!"')

    def voice1(self):
        print(f'{self._name} : "Aku hanya butuh ketenangan dalam hidup ini :)"')
        
    def voice2(self):
        print(f'{self._name} : "Kenapa? Kenapa aku masih terus berurusan dengan manusia?"')
        
class SupportSystem(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'Support System'
        self._health = 5500
        self._power = 150
        self._defense = 2500
        
    def ultimate(self, target):
        self._health += 1000
        self._defense += 500
        if target._defense > 0:
            kondisi1 = self._power * (75/100)
            target._defense -= kondisi1
            kondisi2 = self._power * (25/100)
            target._health -= kondisi2
        else:
            target._health -= self._power
        print('--- Ultimate Support System akan meningkatkan darah')
        print('dan defensenya lalu menyerang targetnya ---\n')
        print(f'{self._name} : "SEMANGAAT!!!"')
        
    def voice1(self):
        print(f'{self._name} : "Selama kamu baik, aku akan selalu mendukungmu"')
        
    def voice2(self):
        print(f'{self._name} : "Ayoo! Kamu pasti bisa!"')

class DilanCepmek(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'Dilan Cepmek'
        self._health = 5300
        self._power = 150
        
    def ultimate(self, target):
        target._health += self._power * (10/100)
        target._defense -= self._power * (10/100)
        if target._defense > 0:
            kondisi1 = self._power * (50/100)
            target._defense -= kondisi1
            kondisi2 = self._power * (50/100)
            target._health -= kondisi2
        else:
            target._health -= self._power
        print('--- Ultimate Dilan Cepmek akan menambah darah dan defense target')
        print('sebanyak 10% dari powernya lalu akan menyerang darah')
        print('dan defense targetnya dengan damage seimbang ---\n')
        print(f'{self._name} : "Biar aku kasih tau ya, jangan lupa join live ya"')
        
    def voice1(self):
        print(f'{self._name} : "Kamu nanya? Kamu nanya? Kamu nanya?"')
        
    def voice2(self):
        print(f'{self._name} : "Kamu bertanya-tanya? Apakah kamu bertanya-tanya?"')
        
class ThePhoenix(Player):
    def __init__(self, name, atribut):
        super().__init__(name, atribut)
        self._class = 'The Phoenix'
        self._health = 6000
        self._power = 700
        self._defense = 2500
        
    def skill1(self, target):
        if target._defense > 0:
            kondisi1 = self._power * (65/100)
            target._defense -= kondisi1
            kondisi2 = self._power * (25/100)
            target._health -= kondisi2
        else:
            self._health += 100
            kondisi2 = self._power * (75/100)
            target._health -= kondisi2
            
    def skill2(self, target):
        kondisi1 = self._power * (65/100)
        target._health -= kondisi1
        
    def ultimate(self, target):
        self._health += 500
        self._power *= 1.5
        self._defense += 250
        target._health -= target._power
        if target._defense > 0:
            target._defense -= (self._power * (25/100)) * 3
        else:
            target._health -= (self._power * (25/100)) * 3
        target._power = 200
        print('--- Ultimate The Phoenix akan meningkatkan atribut-atributnya')
        print('lalu membakar target dan merusak powernya ---\n')
        print(f'{self._name} : "Feel the power of Phoenix"')
        
    def voice1(self):
        print(f'{self._name} : "I am the strongest and most powerful character"')
        
    def voice2(self):
        print(f'{self._name} : "Let me show what The Phoenix can do"')

# interface
def test_voice1(karakter):
    karakter.voice1()
    
def test_voice2(karakter):
    karakter.voice2()
    