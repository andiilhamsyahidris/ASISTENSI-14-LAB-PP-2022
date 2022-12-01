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


# #Class Wizard
# class Wizard(Hero) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._health=90
#         self._armor=10
# class Shaman(Wizard) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power=24
#         self._speed=17
#     def Skill1(self,target) :
#         target._speed -= 8
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         target._speed -= 10
#         target._armor -= 5
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         self._speed += 15
#         target._speed -= 11
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#         self._speed -= 15
#     def Ultimate(self,target) :
#         self._health += 25
#         self._armor += 14
#         self._speed += 22
#         self._power += 19
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
# class Electro(Wizard) : #My Progress Here
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power = 22
#         self._speed=25
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power

# #Class Mecha
# class Mecha(Hero) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._health=100
#         self._armor=42
# class Megatron(Mecha) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power=21
#         self._speed=20
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
# class UltraMagnus(Mecha) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power=23
#         self._speed=24
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power

# #Class Ninja
# class Ninja(Hero) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._health=100
#         self._armor=12
#         self._speed=30
# class Shogun(Ninja) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power = 26
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
# class Samurai(Ninja) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power = 29
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
# class Ronin(Ninja) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power = 24
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power

# #Class Demon
# class Demon(Hero) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._health=100
#         self._armor=34
# class Goblin(Demon) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power=25
#         self._speed=24
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
# class Luzifer(Demon) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power=28
#         self._speed=26
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
# class Dracula(Demon) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power=26
#         self._speed=28
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power

# #Class Shooter
# class Shooter(Hero) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._health=88
#         self._armor=8
# class Archery(Shooter) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power=32
#         self._speed=29
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
# class Spearman(Shooter) :
#     def __init__(self, name, pos_x):
#         super().__init__(name, pos_x)
#         self._power=35
#         self._speed=30
#     def Skill1(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill2(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Skill3(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power
#     def Ultimate(self,target) :
#         if target._armor > 0 :
#             self._power /= target._armor
#         elif target._armor <= 0 :
#             target._armor=1
#             self._power /= target._armor
#         self._power += (self._speed/self._power)
#         target._health -= self._power

# Interface(Polimorfisme)
# def skill(self,target) :
#     self.special(target)