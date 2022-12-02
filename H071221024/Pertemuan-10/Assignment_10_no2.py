from Hero import SemiTank,Titan,Barbarian,Viking,BountyHunter,Assasin,InfoHero,Name,Class,Regen,AttackSkill
a = 0
b = 0
c = 0
j = 0
x = 0
lst=[]
while x == 0 :
    if j == 0 :
        print('='*100)
        print(' '*37 + 'Welcome to The Battlefield')
        print('='*100)
        j = 1
    strt_end = input('Do you want to play this game? Input Start/End: ')
    strt_end = strt_end.upper()
    print('='*100)
    if strt_end == 'START' : 
        for i in range(1,3) :
            print(f'Player {i}')
            inpName = input('Create NickName Hero: ')
            print('='*100)
            a = 1
            lst.append(inpName)
            while a > 0 :
                c = 1
                b = -1
                print('Class Hero List')
                print('1. Tank\n2. Fighter\n3. Slayer')
                try :
                    inpHero = int(input('Pick Class Hero (Input a number): '))
                    print('='*100)
                    if inpHero == 1 :
                        while c > 0 :
                            print('SubClass Hero List')
                            print('1. SemiTank\n2. Titan')
                            try :
                                inpSubHero = int(input('Pick SubClass Hero (Input a number): '))
                                print('='*100)
                                c -= 1
                                if inpSubHero == 1 :
                                    player = SemiTank(inpName,15)
                                    while b < 0 :
                                        Name(player)
                                        Class(player)
                                        InfoHero(player)
                                        sure=input('Are you sure want to pick this Hero? (type yes/no) ')
                                        sure = sure.lower()
                                        print('='*100)
                                        if sure == 'yes' :
                                            b += 1
                                            c -= 1
                                            a = -1
                                            lst.append('Tank')
                                            lst.append(SemiTank)
                                            break
                                        elif sure == 'no' :
                                            a += 1 
                                            b += 1
                                            c -= 1    
                                        else :
                                            print('Please type yes or no')
                                            print('='*100)
                                elif inpSubHero == 2 :
                                    player = Titan(inpName,15)
                                    while b < 0 :
                                        Name(player)
                                        Class(player)
                                        InfoHero(player)
                                        sure=input('Are you sure want to pick this Hero? (type yes/no) ')
                                        sure = sure.lower()
                                        print('='*100)
                                        if sure == 'yes' :
                                            b += 1
                                            c -= 1
                                            a = -1
                                            lst.append('Tank')
                                            lst.append(Titan)
                                            break
                                        elif sure == 'no' :
                                            a += 1 
                                            b += 1
                                            c -= 1    
                                        else :
                                            print('Please type yes or no')
                                            print('='*100)
                                else :
                                    a += 1
                                    c += 1
                                    print('Please Input a number 1-2')
                                    print('='*100)
                            except :
                                a += 1
                                c += 1
                                print('='*100)
                                print('Please type 1-2 ')
                                print('='*100)
                                                                                    # THIS ONE IS THE CORRECT PROGRAM
                    elif inpHero == 2 :
                        while c > 0 :
                            print('SubClass Hero List')
                            print('1. Barbarian\n2. Viking')
                            try :
                                inpSubHero = int(input('Pick SubClass Hero (Input a number): '))
                                print('='*100)
                                c -= 1
                                if inpSubHero == 1 :
                                    player = Barbarian(inpName,15)
                                    while b < 0 :
                                        Name(player)
                                        Class(player)
                                        InfoHero(player)
                                        sure=input('Are you sure want to pick this Hero? (type yes/no) ')
                                        sure = sure.lower()
                                        print('='*100)
                                        if sure == 'yes' :
                                            b += 1
                                            c -= 1
                                            a = -1
                                            lst.append('Fighter')
                                            lst.append(Barbarian)
                                        elif sure == 'no' :
                                            a += 1 
                                            b += 1
                                            c -= 1    
                                        else :
                                            print('Please type yes or no')
                                            print('='*100)
                                elif inpSubHero == 2 :
                                    player = Viking(inpName,15)
                                    while b < 0 :
                                        Name(player)
                                        Class(player)
                                        InfoHero(player)
                                        sure=input('Are you sure want to pick this Hero? (type yes/no) ')
                                        sure = sure.lower()
                                        print('='*100)
                                        if sure == 'yes' :
                                            b += 1
                                            c -= 1
                                            a = -1
                                            lst.append('Fighter')
                                            lst.append(Viking)
                                        elif sure == 'no' :
                                            a += 1 
                                            b += 1
                                            c -= 1    
                                        else :
                                            print('Please type yes or no')
                                            print('='*100)
                                else :
                                    a += 1
                                    c += 1
                                    print('Please Input a number 1-2')
                                    print('='*100)
                            except :
                                a += 1
                                c += 1
                                print('='*100)
                                print('Please type 1-2 ')
                                print('='*100)
                            # THIS ONE IS THE CORRECT PROGRAM

                    elif inpHero == 3 :
                        while c > 0 :
                            print('SubClass Hero List')
                            print('1. Bounty Hunter\n2. Assasin')
                            try :
                                inpSubHero = int(input('Pick SubClass Hero (Input a number): '))
                                print('='*100)
                                c -= 1
                                if inpSubHero == 1 :
                                    player = BountyHunter(inpName,15)
                                    while b < 0 :
                                        Name(player)
                                        Class(player)
                                        InfoHero(player)
                                        sure=input('Are you sure want to pick this Hero? (type yes/no) ')
                                        sure = sure.lower()
                                        print('='*100)
                                        if sure == 'yes' :
                                            b += 1
                                            c -= 1
                                            a = -1
                                            lst.append('Slayer')
                                            lst.append(BountyHunter)
                                        elif sure == 'no' :
                                            a += 1 
                                            b += 1
                                            c -= 1    
                                        else :
                                            print('Please type yes or no')
                                            print('='*100)
                                elif inpSubHero == 2 :
                                    player = Assasin(inpName,15)
                                    while b < 0 :
                                        Name(player)
                                        Class(player)
                                        InfoHero(player)
                                        sure=input('Are you sure want to pick this Hero? (type yes/no) ')
                                        sure = sure.lower()
                                        print('='*100)
                                        if sure == 'yes' :
                                            b += 1
                                            c -= 1
                                            a = -1
                                            lst.append('Slayer')
                                            lst.append(Assasin)
                                        elif sure == 'no' :
                                            a += 1 
                                            b += 1
                                            c -= 1    
                                        else :
                                            print('Please type yes or no')
                                            print('='*100)
                                else :
                                    a += 1
                                    c += 1
                                    print('Please Input a number 1-2')
                                    print('='*100)
                            except :
                                a += 1
                                c += 1
                                print('='*100)
                                print('Please type 1-2 ')
                                print('='*100)
                            # THIS ONE IS THE CORRECT PROGRAM

                    else :
                        print('Please Input a number 1-3')
                        print('='*100)

                except :
                    print('='*100)
                    print('Please Input a number 1-3 ')
                    print('='*100)

        print(' '*40 + 'Welcome to The Arena')
        print('='*100)
        f = 1
        g = 0 #My Progress Here
        h = 0
        d = 0
        w = 0
        while d == 0 :
            if f == 1 :
                detail1 = lst[2](lst[0],15)
                detail2 = lst[5](lst[3],15)
            if f%2==1 :
                print(f'{detail1.nama}\'s turn')
            elif f%2==0 :
                print(f'{detail2.nama}\'s turn')
            print('1. Attack\n2. Regen\n3. Info Hero\n4. End the game')
            try :
                inpArena = int(input('Select the option: '))
                e = 1
                if inpArena == 1 : #Attack
                    if f%2==1 :
                        AttackSkill(detail1,detail2)
                        f += 1
                        print('='*100)
                        if detail2._health<=0 :
                            print(f'{detail2.nama} Death')
                            print(f'{detail1.nama} Win')
                            print('='*100)
                            while w == 0 :
                                again = input('Do you want to play again? (yes/no) ')
                                again = again.lower()
                                if again == 'yes' :
                                    d += 1
                                    w = 1
                                    j = 0
                                    lst.clear()
                                elif again == 'no' :
                                    print('='*100)
                                    print(' '*43 + 'See You Again')
                                    print('='*100)
                                    w = 1
                                    d = 1
                                    x = 1
                                else :
                                    print('='*100)
                                    print('Type yes or no in the input')
                                    print('='*100)
                    elif f%2==0 :
                        AttackSkill(detail2,detail1)
                        f += 1
                        print('='*100)
                        if detail1._health<=0 :
                            print(f'{detail1.nama} Death')
                            print(f'{detail2.nama} Win')
                            print('='*100)
                            while w == 0 :
                                again = input('Do you want to play again? (yes/no) ')
                                again = again.lower()
                                if again == 'yes' :
                                    w = 1
                                    d = 1
                                    j = 0
                                    lst.clear()
                                elif again == 'no' :
                                    print('='*100)
                                    print(' '*43 + 'See You Again')
                                    print('='*100)
                                    w = 1
                                    d = 1
                                    x = 1
                                else :
                                    print('='*100)
                                    print('Type yes or no in the input')
                                    print('='*100)
                elif inpArena == 2 : #Regen
                    if f%2==1 :
                        print('='*100)
                        Regen(detail1)
                        print('='*100)
                        f += 1
                    elif f%2==0 :
                        print('='*100)
                        Regen(detail2)
                        print('='*100)
                        f += 1  
                elif inpArena == 3 : #Detail Hero
                    if f%2==1 :
                        print('='*100)
                        Name(detail1)
                        Class(detail1)
                        InfoHero(detail1)
                        print('='*100)
                    elif f%2==0 :
                        print('='*100)
                        Name(detail2)
                        Class(detail2)
                        InfoHero(detail2)
                        print('='*100)
                elif inpArena == 4 :
                    while e > 0 :
                        end = input('Are you sure want to end the game? (Input yes/no) ')
                        end = end.lower()
                        if end == 'yes' :
                            print('='*100)
                            print(' '*43 + 'See You Again')
                            print('='*100)
                            e = 0
                            d = 1
                            x = 1
                        elif end == 'no' :
                            print('='*100)
                            e = 0
                            continue
                        else :
                            print('='*100)
                            print('Please input yes or no')
                            print('='*100)            
                else :
                    print('='*100)
                    print('Please input a number 1-4 ')
                    print('='*100)
            except :
                print('='*100)
                print('Please input a number 1-4 ')
                print('='*100)

    elif strt_end == 'END' :
        print(' '*43 + 'See You Again')
        print('='*100)
        break
    else :
        print('Please type Start or End')
        print('='*100)