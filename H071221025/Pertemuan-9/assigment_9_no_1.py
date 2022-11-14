from hero import Warrior, Assassin, Support

warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin",pos_x=30)


# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

print(warrior.getMovement())
warrior.setMovement("L")
print(warrior.getMovement())
print("_"*10)
print(warrior.getMovement())

print(assassin.getMovement())
assassin.setMovement("L")
print(assassin.getMovement())
print("_"*10)
print(assassin.getMovement())

print(support.getMovement())
support.setMovement("L")
print(support.getMovement())
print("_"*10)
print(support.getMovement())