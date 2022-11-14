import re

loop=int(input())
listIP=[]
for i in range(loop) :
    adressIP=input()
    listIP.append(adressIP)
for j in range(len(listIP)):
    if '.' in listIP[j] :
        match1=re.search('^(([0-1]?([0-9]?){2}|[0-2]?([0-5]?){2}|[0-2]?[0-4]?[0-9]?).){3}([0-1]?([0-9]?){2}|[0-2]?([0-5]?){2}|[0-2]?[0-4]?[0-9]?)$',listIP[j])
        if match1 :
            print('IPv4')
        else :
            print('Bukan IP Adress')
    elif ':' in listIP[j] :
        match2=re.search('^(([\da-fA-F]?){1,4}:){7}(([\da-fA-F]?){1,4})$',listIP[j])
        if match2 :
            print('IPv6')
        else :
            print('Bukan IP Adress')
    else :
        print('Bukan IP Adress')