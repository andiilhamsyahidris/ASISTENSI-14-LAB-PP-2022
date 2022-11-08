import re

IPv4 = r"^(([0-9]\b.|[0-9]?[0-9]\b.|[0-1]?[0-9]?[0-9]\b.|[2]?[0-5]?[0-5]\b.){3})([0-9]|[0-9]?[0-9]|[0-1]?[0-9]?[0-9]|[2]?[0-5]?[0-5])$"
IPv6 = r"^(([0-9,a-f]{1}\b:|[0-9,a-f]{2}\b:|[0-9,a-f]{3}\b:|[0-9,a-f]{4}\b:){7})([0-9,a-f]{1}|[0-9,a-f]{2}|[0-9,a-f]{3}|[0-9,a-f]{4})$"
n = int(input("Banyak baris : "))
list_IPv = []
for i in range(n) :
    str = input("Masukkan String : ")  
    list_IPv.append(str)
for j in list_IPv :
    result_IPv4 = re.search (IPv4,j) 
    if result_IPv4 :
        print("IPv4")
    else : 
        result_IPv6 = re.search (IPv6,j)
        if result_IPv6 :
            print ("IPv6")
        else :
            print("Bukan IP Address")