import random
import time
import os
o = ''
computer_options = ['rock','paper','scissors']
computer = random.choice(computer_options)
computer_won = 0
human_won = 0
def sax():
    global computer_won
    computer_won += 1
    time.sleep(2)
    print(f'i chose {computer}')
    print('[+]so it seems like i  won')
    print(f'[+]human:{human_won}\ncomputer:{computer_won}')
    os.system('cls')
    
def sax2():
    time.sleep(2)
    global human_won
    human_won += 1
    print('[+]i chose',computer)
    print('[+]you won :sob:')
    print(f'[+]human:{human_won}\ncomputer:{computer_won}')
    time.sleep(6)
    os.system('cls')

while True:
    print('''                                                         (_)                       
 _ __ ___   ___| | __  _ __   __ _ _ __   ___ _ __   ___  ___ _ ___ ___  ___  _ __ ___ 
| '__/ _ \ / __| |/ / | '_ \ / _` | '_ \ / _ \ '__| / __|/ __| / __/ __|/ _ \| '__/ __|
| | | (_) | (__|   <  | |_) | (_| | |_) |  __/ |    \__ \ (__| \__ \__ \ (_) | |  \__ /
|_|  \___/ \___|_|\_\ | .__/ \__,_| .__/ \___|_|    |___/\___|_|___/___/\___/|_|  |___/
                      | |         | |                                                  
                      |_|         |_|                                                  ''')
    s = input('1)rock\n2)paper\n3)scissors\n-type quite to exit the program\n[*]:')
    #im gay(jk)
    if s == 'quit':
        break
    
   
    # converting shit to a number
    if s == 'rock':
        s = '1'
    elif s == 'paper':
        s ='2'
    elif s == 'scissors':
        s = '3'
    #computer wins AHAHAHAHAHHAA
    if computer == 'rock' and s == '3':
        sax()
    elif computer == 'paper' and s == '1':
        sax()
    elif computer == 'sissors' and s == '2':
        sax()

    
    
    # the_human_wins
    if s == '1' and computer == 'scissors':
        sax2()
    elif s == '2' and computer == 'rock':
        sax2()
    elif s == '3' and computer == 'paper':
        sax2()
    # tie uwu
    else:
        print('[+]caluclating results')
        time.sleep(3)
        print(f'[+]the computer chose {computer} too its a tie uwu')
        print(f'[+]human:{human_won}\ncomputer:{computer_won}')
        time.sleep(6)
        os.system('cls')
