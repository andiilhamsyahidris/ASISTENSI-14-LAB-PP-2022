from assignment_10_no2 import Petarunk, Dukun, WadimorBoy, CobuzierMan, BocilLatto
from assignment_10_no2 import OrangDepresi, SupportSystem, DilanCepmek, ThePhoenix
from assignment_10_no2 import test_voice1, test_voice2
import random
import time

def profile():
    print('--- This mini game created by ---')
    time.sleep(0.5)
    print('Name         : Muh. Adnan Putra Amiruddin')
    time.sleep(0.5)
    print('NIM          : H071221080')
    time.sleep(0.7)
    print('You can check my repository at my GitHub')
    time.sleep(0.5)
    print('GitHub       : Mr.Adnan34')
    time.sleep(0.7)
    print('You can also follow my Social Media')
    time.sleep(0.5)
    print('Instagram    : @muh.adnan_putra')
    time.sleep(0.5)
    print('--- Thank you >< ---')

def decoration(num):
    print('='*num*2)
    time.sleep(0.5)
    
def choose_mode():
    print('Mode List:')
    time.sleep(0.5)
    print('1. P1 vs P2\n2. P1 vs Bot\n3. Bot vs Bot')
    
def character_list():
    print('Character List :')
    print('1. Petarunk\n2. Dukun\n3. Wadimor Boy\n4. Cobuzier Man\n5. Bocil Latto')
    time.sleep(0.5)
    print('6. Orang Depresi\n7. Support System\n8. Dilan Cepmek\n9. The Phoenix')

def attributte_list():
    print('Attributte List :')
    print('1. Panci Emak\n2. Milo Energen\n3. Kopi Toraja')
    time.sleep(0.5)
    print('4. Sapu Ibu\n5. Rim Besi\n6. Es Kepal Milo')
    
def ultimate_list():
    print('-- Ultimate Round! --')
    print('Skill List :')
    print('1. Skill 1 (Defense Priority)\n2. Skill 2 (Health Priority)')
    time.sleep(0.5)
    print('3. Ultimate Skill')
    
def skill_list():
    print('Skill List :')
    print('1. Skill 1 (Defense Priority)')
    time.sleep(0.5)
    print('2. Skill 2 (Health Priority)')
    
def status_player1():
    print("--- Player 1's Status Update ---")
    time.sleep(1)
    print('Name         :', player1.getName())
    print('Character    :', player1.getClass())
    print('Attributte   :', player1.getAttribut())
    print('Health       :', player1.getHealth())
    print('Power        :', player1.getPower())

    print('Defense      :', player1.getDefense())
def status_bot1():
    print("--- Bot 1's Status Update ---")
    time.sleep(1)
    print('Name         :', player1.getName())
    print('Character    :', player1.getClass())
    print('Attributte   :', player1.getAttribut())
    print('Health       :', player1.getHealth())
    print('Power        :', player1.getPower())
    print('Defense      :', player1.getDefense())
    
def status_player2():
    print("--- Player 2's Status Update ---")
    time.sleep(1)
    print('Name         :', player2.getName())
    print('Character    :', player2.getClass())
    print('Attributte   :', player2.getAttribut())
    print('Health       :', player2.getHealth())
    print('Power        :', player2.getPower())
    print('Defense      :', player2.getDefense())

def status_bot2():
    print("--- Bot 2's Status Update ---")
    time.sleep(1)
    print('Name         :', player2.getName())
    print('Character    :', player2.getClass())
    print('Attributte   :', player2.getAttribut())
    print('Health       :', player2.getHealth())
    print('Power        :', player2.getPower())
    print('Defense      :', player2.getDefense())
    
def status_bot():
    print("--- Bot's Status Update ---")
    time.sleep(1)
    print('Name         :', player2.getName())
    print('Character    :', player2.getClass())
    print('Attributte   :', player2.getAttribut())
    print('Health       :', player2.getHealth())
    print('Power        :', player2.getPower())
    print('Defense      :', player2.getDefense())
    
def cek_player1():
    print('-- Check Player 1 --')
    time.sleep(0.5)
    print('Damage Received  :', player2.getPower())
    time.sleep(0.3)
    print('Health           :', player1.getHealth())

def cek_bot1():
    print('-- Check Bot 1 --')
    time.sleep(0.5)
    print('Damage Received  :', player2.getPower())
    time.sleep(0.3)
    print('Health           :', player1.getHealth())
    
def cek_player2():
    print('-- Check Player 2 --')
    time.sleep(0.5)
    print('Damage Received  :', player1.getPower())
    time.sleep(0.3)
    print('Health           :', player2.getHealth())

def cek_bot2():
    print('-- Check Bot 2 --')
    time.sleep(0.5)
    print('Damage Received  :', player1.getPower())
    time.sleep(0.3)
    print('Health           :', player2.getHealth())
    
def cek_bot():
    print('-- Check Bot --')
    time.sleep(0.5)
    print('Damage Received  :', player1.getPower())
    time.sleep(0.3)
    print('Health           :', player2.getHealth())

decoration(50)
print('----- Pesona Indonesia Battle -----')
decoration(50)
profile()
decoration(50)
print('--- Welcome to The Mini PVP Game ---\n----- Have Fun Guysz -----')
decoration(50)

choose_mode()
choose = input('Mode (Choose the number) : ')
decoration(50)
if choose == '1':
    print("--- Playing by your friend ---")
    decoration(50)
    
    name1 = input('Player 1 name : ')
    decoration(30)
    character_list()
    decoration(30)
    
    karakter1 = input('Choose character for player 1 : ')
    decoration(30)
    attributte_list()
    decoration(30)
    
    atribut1 = input('Player 1 attribute : ')
    if atribut1 == '1':
        atribut1 = 'Panci Emak'
    elif atribut1 == '2':
        atribut1 = 'Milo Energen'
    elif atribut1 == '3':
        atribut1 = 'Kopi Toraja'
    elif atribut1 == '4':
        atribut1 = 'Sapu Ibu'
    elif atribut1 == '5':
        atribut1 = 'Rim Besi'
    elif atribut1 == '6':
        atribut1 = 'Es Kepal Milo'
    else:
        print('Input of attribute list number is not correct\nExit the game...')
        exit()

    if karakter1 == '1':
        player1 = Petarunk(name1, atribut1)
    elif karakter1 == '2':
        player1 = Dukun(name1, atribut1)
    elif karakter1 == '3':
        player1 = WadimorBoy(name1, atribut1)
    elif karakter1 == '4':
        player1 = CobuzierMan(name1, atribut1)
    elif karakter1 == '5':
        player1 = BocilLatto(name1, atribut1)
    elif karakter1 == '6':
        player1 = OrangDepresi(name1, atribut1)
    elif karakter1 == '7':
        player1 = SupportSystem(name1, atribut1)
    elif karakter1 == '8':
        player1 = DilanCepmek(name1, atribut1)
    elif karakter1 == '9':
        player1 = ThePhoenix(name1, atribut1)
    else:
        print('Input of character list number is not correct\nExit the game...')
        exit()

    decoration(30)
    player1.setAtribut()
    status_player1()
    decoration(30)
    time.sleep(2)
    
    test_voice1(player1)
    decoration(50)
    time.sleep(2)
    
    name2 = input('Player 2 name : ')
    decoration(30)
    character_list()
    decoration(30)
    
    karakter2 = input('Choose character for player 2 : ')
    decoration(30)
    attributte_list()
    decoration(30)
    
    atribut2 = input('Player 2 attribute : ')
    if atribut2 == '1':
        atribut2 = 'Panci Emak'
    elif atribut2 == '2':
        atribut2 = 'Milo Energen'
    elif atribut2 == '3':
        atribut2 = 'Kopi Toraja'
    elif atribut2 == '4':
        atribut2 = 'Sapu Ibu'
    elif atribut2 == '5':
        atribut2 = 'Rim Besi'
    elif atribut2 == '6':
        atribut2 = 'Es Kepal Milo'
    else:
        print('Input of attribute list number is not correct\nExit the game...')
        exit()

    if karakter2 == '1':
        player2 = Petarunk(name2, atribut2)
    elif karakter2 == '2':
        player2 = Dukun(name2, atribut2)
    elif karakter2 == '3':
        player2 = WadimorBoy(name2, atribut2)
    elif karakter2 == '4':
        player2 = CobuzierMan(name2, atribut2)
    elif karakter2 == '5':
        player2 = BocilLatto(name2, atribut2)
    elif karakter2 == '6':
        player2 = OrangDepresi(name2, atribut2)
    elif karakter2 == '7':
        player2 = SupportSystem(name2, atribut2)
    elif karakter2 == '8':
        player2 = DilanCepmek(name2, atribut2)
    elif karakter2 == '9':
        player2 = ThePhoenix(name2, atribut2)
    else:
        print('Input of character list number is not correct')
        exit()

    decoration(30)
    player2.setAtribut()
    status_player2()
    decoration(30)
    time.sleep(2)
    
    test_voice1(player2)
    decoration(50)
    time.sleep(2)
    
    print('-'*40*2*2)
    print('Let The Battle Begin!!!')
    print('-'*40*2*2)
    decoration(50)
    print('Loading...')
    time.sleep(2.5)

    lap = 1
    while True:
        if player1.getHealth() <= 0:
            decoration(50)
            print(f'The Winner is {player2.getName()} by Character {player2.getClass()} as Player 2')
            decoration(50)
            print('\nExit the game...')
            time.sleep(3)
            break
        if player2.getHealth() <= 0:
            decoration(50)
            print(f'The Winner is {player1.getName()} by Character {player1.getClass()} as Player 1')
            decoration(50)
            print('\nExit the game...')
            time.sleep(3)
            break
        decoration(30)
        print(f'--- Round {lap} Start ---')
        decoration(30)
        time.sleep(1)
        
        if lap % 3 == 0:
            print("Player 1's turn")
            decoration(30)
            test_voice2(player1)
            decoration(30)
            time.sleep(2)
            
            ultimate_list()
            decoration(30)
            skill = input('Choose 1 skill for attack enemy : ')
            if skill == '1':
                player1.skill1(player2)
            elif skill == '2':
                player1.skill2(player2)
            elif skill == '3':
                player1.ultimate(player2)
                time.sleep(3)
                
            decoration(30)
            cek_player2()
            time.sleep(2)
            
            decoration(30)
            print("Player's 2 turn")
            decoration(30)
            test_voice2(player2)
            decoration(30)
            time.sleep(2)
            
            ultimate_list()
            decoration(30)
            skill = input('Choose 1 skill for attack enemy : ')
            if skill == '1':
                player2.skill1(player1)
            elif skill == '2':
                player2.skill2(player1)
            elif skill == '3':
                player2.ultimate(player1)
                time.sleep(3)
                
            decoration(30)
            cek_player1()
            time.sleep(2)
        else:
            print("Player 1's turn")
            decoration(30)
            test_voice2(player1)
            decoration(30)
            time.sleep(2)
            
            skill_list()
            decoration(30)
            skill = input('Choose 1 skill for attack enemy : ')
            if skill == '1':
                player1.skill1(player2)
            elif skill == '2':
                player1.skill2(player2)
            
            decoration(30)
            cek_player2()
            time.sleep(2)
            
            decoration(30)
            print("Player's 2 turn")
            decoration(30)
            test_voice2(player2)
            decoration(30)
            time.sleep(2)
            
            skill_list()
            decoration(30)
            skill = input('Choose 1 skill for attack enemy : ')
            if skill == '1':
                player2.skill1(player1)
            elif skill == '2':
                player2.skill2(player1)
                
            decoration(30)
            cek_player1()
            time.sleep(2)
        
        decoration(50)
        print(f'----- Round {lap} Finished -----')
        decoration(50)
        print('Counting the result...')
        time.sleep(3)
        decoration(30)
        print('Wanna Check It?\n1. Yes\n2. No')
        check = input('Answer (input "1" or "2") : ')
        if check == '1':
            decoration(30)
            status_player1()
            decoration(30)
            time.sleep(3)
            status_player2()
            time.sleep(3)
        else:
            None
        lap += 1
            
elif choose == '2':
    print("--- Playing by computer's bot ---")
    decoration(50)
    
    name1 = input('Player 1 name : ')
    decoration(30)
    character_list()
    decoration(30)
    
    karakter1 = input('Choose character for player 1 : ')
    decoration(30)
    attributte_list()
    decoration(30)
    
    atribut1 = input('Player 1 attribute : ')
    if atribut1 == '1':
        atribut1 = 'Panci Emak'
    elif atribut1 == '2':
        atribut1 = 'Milo Energen'
    elif atribut1 == '3':
        atribut1 = 'Kopi Toraja'
    elif atribut1 == '4':
        atribut1 = 'Sapu Ibu'
    elif atribut1 == '5':
        atribut1 = 'Rim Besi'
    elif atribut1 == '6':
        atribut1 = 'Es Kepal Milo'
    else:
        print('Input of attribute list number is not correct\nExit the game...')
        exit()

    if karakter1 == '1':
        player1 = Petarunk(name1, atribut1)
    elif karakter1 == '2':
        player1 = Dukun(name1, atribut1)
    elif karakter1 == '3':
        player1 = WadimorBoy(name1, atribut1)
    elif karakter1 == '4':
        player1 = CobuzierMan(name1, atribut1)
    elif karakter1 == '5':
        player1 = BocilLatto(name1, atribut1)
    elif karakter1 == '6':
        player1 = OrangDepresi(name1, atribut1)
    elif karakter1 == '7':
        player1 = SupportSystem(name1, atribut1)
    elif karakter1 == '8':
        player1 = DilanCepmek(name1, atribut1)
    elif karakter1 == '9':
        player1 = ThePhoenix(name1, atribut1)
    else:
        print('Input of character list number is not correct\nExit the game...')
        exit()

    decoration(30)
    player1.setAtribut()
    status_player1()
    decoration(30)
    time.sleep(2)
    
    test_voice1(player1)
    decoration(50)
    time.sleep(2)
    
    print("It's the bot's turn...")
    time.sleep(1.5)
    name2 = 'Computer'
    decoration(30)
    print(f'Bot 1 name : {name2}')
    time.sleep(1)
    
    decoration(30)
    character_list()
    decoration(30)
    time.sleep(2)
    
    karakter2 = random.randint(1, 9)
    print(f'Computer chose character number : {karakter2}')
    time.sleep(1)
    
    decoration(30)
    attributte_list()
    decoration(30)
    time.sleep(2)
    
    atribut2 = random.randint(1, 6)
    print(f'Computer chose attributte number : {atribut2}')
    time.sleep(1)
    if atribut2 == 1:
        atribut2 = 'Panci Emak'
    elif atribut2 == 2:
        atribut2 = 'Milo Energen'
    elif atribut2 == 3:
        atribut2 = 'Kopi Toraja'
    elif atribut2 == 4:
        atribut2 = 'Sapu Ibu'
    elif atribut2 == 5:
        atribut2 = 'Rim Besi'
    elif atribut2 == 6:
        atribut2 = 'Es Kepal Milo'
    else:
        print('Input of attribute list number is not correct\nExit the game...')
        exit()

    if karakter2 == 1:
        player2 = Petarunk(name2, atribut2)
    elif karakter2 == 2:
        player2 = Dukun(name2, atribut2)
    elif karakter2 == 3:
        player2 = WadimorBoy(name2, atribut2)
    elif karakter2 == 4:
        player2 = CobuzierMan(name2, atribut2)
    elif karakter2 == 5:
        player2 = BocilLatto(name2, atribut2)
    elif karakter2 == 6:
        player2 = OrangDepresi(name2, atribut2)
    elif karakter2 == 7:
        player2 = SupportSystem(name2, atribut2)
    elif karakter2 == 8:
        player2 = DilanCepmek(name2, atribut2)
    elif karakter2 == 9:
        player2 = ThePhoenix(name2, atribut2)
    else:
        print('Input of character list number is not correct\nExit the game...')
        exit()

    decoration(30)
    player2.setAtribut()
    status_player2()
    decoration(30)
    time.sleep(2)
    
    test_voice1(player2)
    decoration(50)
    time.sleep(2)
    
    print('-'*40*2)
    print('Let The Battle Begin!!!')
    print('-'*40*2)
    decoration(50)
    print('Loading...')
    time.sleep(2.5)

    lap = 1
    while True:
        if player1.getHealth() <= 0:
            decoration(50)
            print(f'The Winner is {player2.getName()} by Character {player2.getClass()} as Bot')
            decoration(50)
            print('\nExit the game...')
            time.sleep(3)
            break
        if player2.getHealth() <= 0:
            decoration(50)
            print(f'The Winner is {player1.getName()} by Character {player1.getClass()} as Player 1')
            decoration(50)
            print('\nExit the game...')
            time.sleep(3)
            break
        decoration(30)
        print(f'--- Round {lap} Start ---')
        decoration(30)
        time.sleep(1)
        
        if lap % 3 == 0:
            print("Player 1's turn")
            decoration(30)
            test_voice2(player1)
            decoration(30)
            time.sleep(2)
            
            ultimate_list()
            decoration(30)
            skill = input('Choose 1 skill for attack enemy : ')
            if skill == '1':
                player1.skill1(player2)
            elif skill == '2':
                player1.skill2(player2)
            elif skill == '3':
                player1.ultimate(player2)
                time.sleep(3)
                
            decoration(30)
            cek_bot()
            time.sleep(2)
            
            decoration(30)
            print("Bot's turn...")
            decoration(30)
            test_voice2(player2)
            decoration(30)
            time.sleep(2)
            
            ultimate_list()
            decoration(30)
            skill = 3
            print(f'Computer chose skill number : {skill}')
            time.sleep(1)
            if skill == 1:
                player2.skill1(player1)
            elif skill == 2:
                player2.skill2(player1)
            elif skill == 3:
                player2.ultimate(player1)
                time.sleep(3)
                
            decoration(30)
            cek_player1()
            time.sleep(2)
            
        else:
            print("Player 1's turn")
            decoration(30)
            test_voice2(player1)
            decoration(30)
            time.sleep(2)
            
            skill_list()
            decoration(30)
            skill = input('Choose 1 skill for attack enemy : ')
            if skill == '1':
                player1.skill1(player2)
            elif skill == '2':
                player1.skill2(player2)
                
            decoration(30)
            cek_bot()
            time.sleep(2)
            
            decoration(30)
            print("Bot's turn...")
            decoration(30)
            test_voice2(player2)
            decoration(30)
            time.sleep(2)
            
            skill_list()
            decoration(30)
            skill = random.randint(1, 2)
            print(f'Computer chose skill number : {skill}')
            time.sleep(1)
            if skill == 1:
                player2.skill1(player1)
            elif skill == 2:
                player2.skill2(player1)
                
            decoration(30)
            cek_player1()
            time.sleep(2)
        
        decoration(50)
        print(f'----- Round {lap} Finished -----')
        decoration(50)
        print('Counting the result...')
        time.sleep(3)
        print('Wanna Check It?\n1. Yes\n2. No')
        check = input('Answer (input "1" or "2") : ')
        if check == '1':
            decoration(30)
            status_player1()
            decoration(30)
            time.sleep(3)
            status_bot()
            time.sleep(3)
        else:
            None
        lap += 1
        
elif choose == '3':
    print("--- Watching bot vs bot ---")
    decoration(50)
    
    print("It's the first bot's turn...")
    time.sleep(1.5)
    name1 = 'Computer1'
    decoration(30)
    print(f"Bot 1's name : {name1}")
    time.sleep(1)
    
    decoration(30)
    character_list()
    decoration(30)
    
    karakter1 = input('Choose character for bot 1 : ')
    decoration(30)
    attributte_list()
    decoration(30)
    
    atribut1 = input('Bot 1 attribute : ')
    if atribut1 == '1':
        atribut1 = 'Panci Emak'
    elif atribut1 == '2':
        atribut1 = 'Milo Energen'
    elif atribut1 == '3':
        atribut1 = 'Kopi Toraja'
    elif atribut1 == '4':
        atribut1 = 'Sapu Ibu'
    elif atribut1 == '5':
        atribut1 = 'Rim Besi'
    elif atribut1 == '6':
        atribut1 = 'Es Kepal Milo'
    else:
        print('Input of attribute list number is not correct\nExit the game...')
        exit()

    if karakter1 == '1':
        player1 = Petarunk(name1, atribut1)
    elif karakter1 == '2':
        player1 = Dukun(name1, atribut1)
    elif karakter1 == '3':
        player1 = WadimorBoy(name1, atribut1)
    elif karakter1 == '4':
        player1 = CobuzierMan(name1, atribut1)
    elif karakter1 == '5':
        player1 = BocilLatto(name1, atribut1)
    elif karakter1 == '6':
        player1 = OrangDepresi(name1, atribut1)
    elif karakter1 == '7':
        player1 = SupportSystem(name1, atribut1)
    elif karakter1 == '8':
        player1 = DilanCepmek(name1, atribut1)
    elif karakter1 == '9':
        player1 = ThePhoenix(name1, atribut1)
    else:
        print('Input of character list number is not correct\nExit the game...')
        exit()

    decoration(30)
    player1.setAtribut()
    status_bot1()
    decoration(30)
    time.sleep(2)
    
    test_voice1(player1)
    decoration(50)
    time.sleep(2)
    
    print("It's the second bot's turn...")
    time.sleep(1.5)
    name2 = 'Computer2'
    decoration(30)
    print(f"Bot 2's name : {name2}")
    time.sleep(1)
    
    decoration(30)
    character_list()
    decoration(30)
    
    karakter2 = input('Choose character for bot 2 : ')
    decoration(30)
    attributte_list()
    decoration(30)
    
    atribut2 = input('Bot 2 attribute : ')
    if atribut2 == '1':
        atribut2 = 'Panci Emak'
    elif atribut2 == '2':
        atribut2 = 'Milo Energen'
    elif atribut2 == '3':
        atribut2 = 'Kopi Toraja'
    elif atribut2 == '4':
        atribut2 = 'Sapu Ibu'
    elif atribut2 == '5':
        atribut2 = 'Rim Besi'
    elif atribut2 == '6':
        atribut2 = 'Es Kepal Milo'
    else:
        print('Input of attribute list number is not correct\nExit the game...')
        exit()

    if karakter2 == '1':
        player2 = Petarunk(name2, atribut2)
    elif karakter2 == '2':
        player2 = Dukun(name2, atribut2)
    elif karakter2 == '3':
        player2 = WadimorBoy(name2, atribut2)
    elif karakter2 == '4':
        player2 = CobuzierMan(name2, atribut2)
    elif karakter2 == '5':
        player2 = BocilLatto(name2, atribut2)
    elif karakter2 == '6':
        player2 = OrangDepresi(name2, atribut2)
    elif karakter2 == '7':
        player2 = SupportSystem(name2, atribut2)
    elif karakter2 == '8':
        player2 = DilanCepmek(name2, atribut2)
    elif karakter2 == '9':
        player2 = ThePhoenix(name2, atribut2)
    else:
        print('Input of character list number is not correct\nExit the game...')
        exit()

    decoration(30)
    player2.setAtribut()
    status_bot2()
    decoration(30)
    time.sleep(2)
    
    test_voice1(player2)
    decoration(50)
    time.sleep(2)
    
    print('-'*40*2)
    print('Let The Battle Begin!!!')
    print('-'*40*2)
    decoration(50)
    print('Loading...')
    time.sleep(2.5)

    lap = 1
    while True:
        if player1.getHealth() <= 0:
            decoration(50)
            print(f'The Winner is {player2.getName()} by Character {player2.getClass()} as Bot 2')
            decoration(50)
            print('\nExit the game...')
            time.sleep(3)
            break
        if player2.getHealth() <= 0:
            decoration(50)
            print(f'The Winner is {player1.getName()} by Character {player1.getClass()} as Bot 1')
            decoration(50)
            print('\nExit the game...')
            time.sleep(3)
            break
        decoration(30)
        print(f'--- Round {lap} Start ---')
        decoration(30)
        time.sleep(1)
        
        if lap % 3 == 0:
            print("Bot 1's turn...")
            decoration(30)
            test_voice2(player1)
            decoration(30)
            time.sleep(2)
            
            ultimate_list()
            decoration(30)
            skill = 3
            print(f'Computer1 chose skill number : {skill}')
            time.sleep(1)
            if skill == 1:
                player1.skill1(player2)
            elif skill == 2:
                player1.skill2(player2)
            elif skill == 3:
                player1.ultimate(player2)
                time.sleep(3)
                
            decoration(30)
            cek_bot2()
            time.sleep(2)
            
            decoration(30)
            print("Bot 2's turn...")
            decoration(30)
            test_voice2(player2)
            decoration(30)
            time.sleep(2)
            
            ultimate_list()
            decoration(30)
            skill = 3
            print(f'Computer2 chose skill number : {skill}')
            time.sleep(1)
            if skill == 1:
                player2.skill1(player1)
            elif skill == 2:
                player2.skill2(player1)
            elif skill == 3:
                player2.ultimate(player1)
                time.sleep(3)
                
            decoration(30)
            cek_bot1()
            time.sleep(2)
            
        else:
            print("Bot 1's turn...")
            decoration(30)
            test_voice2(player1)
            decoration(30)
            time.sleep(2)
            
            skill_list()
            decoration(30)
            skill = random.randint(1, 2)
            print(f'Computer1 chose skill number : {skill}')
            time.sleep(1)
            if skill == 1:
                player1.skill1(player2)
            elif skill == 2:
                player1.skill2(player2)
                
            decoration(30)
            cek_bot2()
            time.sleep(2)
            
            decoration(30)
            print("Bot 2's turn...")
            decoration(30)
            test_voice2(player2)
            decoration(30)
            time.sleep(2)
            
            skill_list()
            decoration(30)
            skill = random.randint(1, 2)
            print(f'Computer2 chose skill number : {skill}')
            time.sleep(1)
            if skill == 1:
                player2.skill1(player1)
            elif skill == 2:
                player2.skill2(player1)
                
            decoration(30)
            cek_bot1()
            time.sleep(2)
        
        decoration(50)
        print(f'----- Round {lap} Finished -----')
        decoration(50)
        print('Counting the result...')
        time.sleep(3)
        print('Wanna Check It?\n1. Yes\n2. No')
        time.sleep(1)
        print('Choosing...')
        time.sleep(1.5)
        check = random.randint(1, 2)
        print(f'Computer chose number : {check}')
        time.sleep(0.5)
        if check == 1:
            decoration(30)
            status_bot1()
            decoration(30)
            time.sleep(3)
            status_bot2()
            time.sleep(3)
        else:
            None
        lap += 1
        
else:
    print('Input of mode number is not correct\n\nExit the game...')
    exit()
