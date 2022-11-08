# IZZATA CLARISSA SALSABILA
# H071221065
# Mengecek sebuah string S

import re

try :
    stringS = input("masukkan string S: ")
    pattern = re.search("[2468a-zA-Z]{40}[13579\s]{5}", stringS)
    if pattern :
        print("True")
    else : 
        print("False")
except:
   print("False")