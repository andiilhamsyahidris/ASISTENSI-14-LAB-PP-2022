# Mengindentifikasikan sebuah perangkat pada internet atau jaringan seluler

import re

def ipv4 (ip) :
    pola1= r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    match1 = fr"{pola1}\.{pola1}\.{pola1}\.{pola1}"
    return re.fullmatch (match1,ip)

def ipv6 (ip) :
    pola2 = r"([0-9A-Fa-f]{1,4})"
    match2 = fr"{pola2}:{pola2}:{pola2}:{pola2}:{pola2}:{pola2}:{pola2}:{pola2}"
    return re.fullmatch (match2,ip)

loop=int(input())
listIP=[]

for i in range(loop) :
    adressIP=input()
    listIP.append(adressIP)
for j in listIP:
    if ipv4 (j) :
        print ("IPv4")
    elif ipv6 (j) :
        print ("IPv6")
    else :
        print ("Bukan IP Address")

#input 1 
# 3
# This line has trailing whitespace
# 121.203.190.20
# 2001:0db8:0000:0000:0000:ff00:0042:8329

#input 2
# 3
# 213.214.111.564
# 444.444.444.444 not an ip address
# 1050:0:0a:600:300c:326b
