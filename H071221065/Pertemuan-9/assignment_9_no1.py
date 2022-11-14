from hero import Warrior, Assassin, Support

warrior  = Warrior("ganyu", pos_x=10)
assassin = Assassin("diluc", pos_x=25)
support  = Support("xiangling", pos_x=30)

#sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
#sesudah
print("health (after)", warrior.getHealth())

print("-"*10)

#sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) :", support.getSpeed())

support.special(warrior)

#sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed) :", support.getSpeed())

print (warrior.getMovement())
warrior.setMovement("R")
print (warrior.getMovement())
print ("-"*10)

print (assassin.getMovement())
assassin.setMovement("R")
print (assassin.getMovement())
print ("-"*10)
print (assassin.getMovement())

print (support.getMovement())
support.setMovement("R")
print (support.getMovement())
print ("-"*10)
