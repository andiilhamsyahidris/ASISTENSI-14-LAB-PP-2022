from abc import ABC, abstractmethod
#Abstract Class 
class Human(ABC) :
    @abstractmethod
    def __init__(self,name,pos_x) :
        self.nama=name
        self.__posisi=pos_x

    def setMovement(self,set) :
        set=set.upper()
        if set=='L' :
            self.__posisi-=self._speed
        if set=='R' :
            self.__posisi+=self._speed
    def getMovement(self) :
        print(self.__posisi)

    @abstractmethod
    def getPower(self) :
        pass
    @abstractmethod
    def getHealth(self) :
        pass
    @abstractmethod
    def getArmor(self) :
        pass
    @abstractmethod
    def getSpeed(self) :
        pass       

#Class Hero
class Hero(Human) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power=10
        self._health=100
        self._armor=5
        self._speed=3
    def getPower(self) :
        return self._power
    def getHealth(self) :
        return self._health
    def getArmor(self) :
        return self._armor
    def getSpeed(self) :
        return self._speed

#Class Tank
class Tank(Hero) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health=120
        self._armor=50
class SemiTank(Tank) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power=15
        self._speed=10
    def Ultimate(self,target) :
        target._armor -= 10
        if target._armor > 0 :
            self._power /= target._armor
        elif target._armor <= 0 :
            target._armor=1
            self._power /= target._armor
        target._health -= self._power
        print('Damage Incurred:', self._power)
        print(f'Remaining Health Target: {target._health} (-{self._power})')
        self._power = 15
class Titan(Tank) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power=18
        self._speed=7
    def Ultimate(self,target) :
        target._armor -= 12
        if target._armor > 0 :
            self._power /= target._armor
        elif target._armor <= 0 :
            target._armor=1
            self._power /= target._armor
        target._health -= self._power
        print('Damage Incurred:', self._power)
        print(f'Remaining Health Target: {target._health} (-{self._power})')
        self._power = 18 #THIS IS THE CORRECT PROGRAM

#Class Fighter
class Fighter(Hero) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health=100
        self._power=20
class Barbarian(Fighter) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._armor=27
        self._speed=8  
    def Ultimate(self,target) :
        target._armor -= 15
        if target._armor > 0 :
            self._power //= target._armor
        elif target._armor <= 0 :
            target._armor=1
            self._power //= target._armor
        target._health -= self._power
        print('Damage Incurred:', self._power)
        print(f'Remaining Health Target: {target._health} (-{self._power})')
        self._power = 20
class Viking(Fighter) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._armor=30
        self._speed=7
    def Ultimate(self,target) :
        target._armor -= 20
        if target._armor > 0 :
            self._power //= target._armor
        elif target._armor <= 0 :
            target._armor=1
            self._power //= target._armor
        target._health -= self._power
        print('Damage Incurred:', self._power)
        print(f'Remaining Health Target: {target._health} (-{self._power})')
        self._power = 20
    
#Class Slayer
class Slayer(Hero) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health=100
class BountyHunter(Slayer) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power=25
        self._armor=15
        self._speed=17
    def Ultimate(self,target) :
        target._armor -= 20
        if target._armor > 0 :
            self._power //= target._armor
        elif target._armor <= 0 :
            target._armor=1
            self._power //= target._armor
        target._health -= self._power
        print('Damage Incurred:', self._power)
        print(f'Remaining Health Target: {target._health} (-{self._power})')
        self._power = 25
class Assasin(Slayer) : 
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power=28
        self._armor=13
        self._speed=20
    def Ultimate(self,target) :
        target._armor -= 15
        if target._armor > 0 :
            self._power //= target._armor
        elif target._armor <= 0 :
            target._armor=1
            self._power //= target._armor
        target._health -= self._power
        print('Damage Incurred:', self._power)
        print(f'Remaining Health Target: {target._health} (-{self._power})')
        self._power = 28

#Interface
def AttackSkill(self,target):
    self.Ultimate(target)
def Regen(self) :
    self._health += 20
    print('Health: ' + str(self._health) + ' (+20)')
def Name(self) :
    print('Name Hero:', self.nama)
def Class(self):
    immediate_parents = type(self).__bases__
    print('Class Hero:',immediate_parents[0].__name__)
def InfoHero(self) :
    print('SubClass Hero:', self.__class__.__name__)
    print('Health:', self.getHealth())
    print('Armor:', self.getArmor())
    print('Power:', self.getPower())
    print('Speed:', self.getSpeed())