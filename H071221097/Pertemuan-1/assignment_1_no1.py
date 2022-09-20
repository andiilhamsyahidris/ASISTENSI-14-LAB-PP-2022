#program01
print ("=================")
print ("Muhammad fadhil abdillah")
print ("H071221097")
#import module

import math
 
h = int(input("input ketinggian menara (h): "))
a = int(input("input sudut elevasi pengamat terhadap ujung depan kapal (a): "))
b = int(input("input sudut elevasi pengamat terhadap ujung belakang kapal (b): "))

#sudut ujung kapal (tan b) = depan/samping = h/b
#sudut ujung belakang kapal ( tan a) = h/b

depan_kapal = h * (math.tan(math.radians(b)))
belakang_kapal = h* (math.tan(math.radians(a)))
panjang = math.sqrt(math.pow(belakang_kapal - depan_kapal,2))

print ("panjang kapal adalah" , round(panjang,1) , "m")