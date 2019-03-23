#!/usr/bin/env  python3
import  random
import  getpass

all_choice = [ 'rock', 'clipper', 'cloth' ]
print(all_choice,end=' --all_choice\n')

win_list = [['rock','clipper'],['clipper','cloth'],['cloth','rock']]
print(win_list,end=' --win_list\n')

prompt = """[0] rock
[1] clipper
[2] cloth
Please input  number( 0|1|2):"""

computer = random.choice(all_choice)
print(computer,type(computer),end=' --computer type\n')

index = int(getpass.getpass("Tip:"+prompt))
print(index,type(index),sep = ' ---- ',end=' --index type\n')

if index > 2 or index < 0:
  print(index,type(index),sep = ' ---- ',end=' --index type\n')
  print('\033[34;1mPossible input error!!!\033[0m')
else:
  player = all_choice[index]
  print(player,type(player),sep = ' ---- ',end=' ---player type\n')
  print("your choice: %s,\tcomputer's choice: %s" % (player,computer))

  if [ player, computer ] in  win_list:
    print('\033[32;1m You as player WIN !\033[0m')
  elif [player,computer] not in win_list:
    if player == computer:
      print("\033[33;1mPlayer equal Computer\033[0m")
    elif [computer,player] in win_list:
      print("\033[31;1m Computer win and you lose!\033[0m")
    else:
      print('\033[34;1mPossible other errors!!!\033[0m')
