#!/usr/bin/env  python3
import  random
import  getpass

def  guess():
  num = random.randint(1,4)
  runboolean = True
  print(type(num),end=' --num type\n')
  print("num is\t" + str(num))

  while runboolean:
    result = int(getpass.getpass('Guess the number: '))
    if result > num:
      print('Too Bigger')
    elif result < num:
      print('Too Smaller')
    else:
      print("Guess Rightly!")
      runboolean = False
      print(runboolean,type(runboolean))

  print("num is\t" + str(num))
