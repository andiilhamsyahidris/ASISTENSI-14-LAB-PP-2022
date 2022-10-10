def robot(x,y) :
    a=0
    while True :
        a+=1
        inputan=input().upper()
        if inputan == 'END' :
            print('exit')
            break
        if a == 1 :
            print(x,y)
        else:
            inputan= list(inputan)
        for i in inputan :
            if i == 'R' :
                x+=1
                print(x,y)
            elif i == 'L' :
                x-=1
                print(x,y)
            elif i == 'U' :
                y+=1
                print(x,y)
            elif i == 'D' :
                y-=1
                print(x,y)
            else :
                continue

robot(0,0)