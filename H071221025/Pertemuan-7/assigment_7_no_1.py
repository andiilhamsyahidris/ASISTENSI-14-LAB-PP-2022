import re

try:
    nilai = input("masukkan nilai: ")
    print(len(nilai))
    if len(nilai)==45:
        pattern = re.match("[2468a-zA-Z]{40}[13579 ]{5}", nilai)
        if pattern :
            print("true")
        else:
            print("false")
    else:
        print("false")
except:
    print("false")