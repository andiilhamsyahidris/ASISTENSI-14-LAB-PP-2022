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
print("-"*10)
# sebelum
print ("Warrior (position)",warrior.getMovement())
warrior.setMovement("L")
# sesudah
print ("Warrior (position)",warrior.getMovement())
print("-"*10)
# sebelum
print ("Assassin (position)",assassin.getMovement())
assassin.setMovement("L") 
# sesudah
print ("Assassin (position)",assassin.getMovement())
print("-"*10)
# sebelum
print ("Support (position)",support.getMovement())
support.setMovement("L")
# sesudah
print ("Support (position)",support.getMovement())