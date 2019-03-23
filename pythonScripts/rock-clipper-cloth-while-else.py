#!/usr/bin/env  python3
import  random
import  getpass

all_choice = [ 'rock', 'clipper', 'cloth' ]
print("All choice  is all_choice = ",all_choice)

win_list = [['rock','clipper'],['clipper','cloth'],['cloth','rock']]
print("win_list  is  ----",win_list)

playdirectory = { 'a': 'rock', 'b': 'clipper', 'c': 'cloth' }
print("playdirectory is  ",playdirectory)

prompt = "[a] rock\n\
[b] clipper\n\
[c] cloth\n\
Please input string( a | b | c ):"

player_frequency , draw, computer_frequency = 0, 0, 0
booleanrun = True

while booleanrun:
  computer = random.choice(all_choice)
  print("computer is  %s  " % computer , type(computer),end=' --computer type\n')
  
  key = getpass.getpass("Tip:"+prompt)
  print("key is  %s \t key type  is " % key , type(key))
  
  if key in 'abc' and len(key) == 1 :
    player = playdirectory[key]
    print(player,type(player),sep = ' ---- ',end=' ---player type\n')
    print("your choice: %s,\tcomputer's choice: %s" % (player,computer))
  
    if [ player, computer ] in  win_list:
      print('\033[32;1m You as player WIN !\033[0m')
      player_frequency += 1
    elif [player,computer] not in win_list:
      if player == computer:
        print("\033[33;1mPlayer equal Computer\033[0m")
        draw += 1
      elif [computer,player] in win_list:
        print("\033[31;1m Computer win and you lose!\033[0m")
        computer_frequency += 1
    print("player_frequency : computer_frequency %s : %s" % (player_frequency + draw , computer_frequency + draw ))
  else:
    print(key,type(key),sep = ' ---- ',end=' --key type\n')
    print('\033[34;1mPossible input error!!!\033[0m')
    break
  if  player_frequency + draw == 3 or computer_frequency + draw == 3:
    if player_frequency > computer_frequency :
      print("player win  player_frequency : computer_frequency %s : %s" % (player_frequency, computer_frequency))
      booleanrun = False
    elif player_frequency < computer_frequency :
      print("Computer win  player_frequency : computer_frequency %s : %s" % (player_frequency, computer_frequency))
      booleanrun = False
    else:
      print("You tied with the computer  player_frequency : computer_frequency %s : %s" % (player_frequency, computer_frequency))
      booleanrun = False
else:
  print("END player_frequency : computer_frequency %s : %s" % (player_frequency, computer_frequency))
