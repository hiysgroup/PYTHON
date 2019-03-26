#!/usr/bin/env   python3
import  random
import  getpass
import  sys
def  function():
  print("\033[33;1m*#yellow* \033[0m" * 10)
  length = int(getpass.getpass('\033[30;43;1m input digital length: \033[0m'))
  
  print('\033[31;1m The integer length is %d  red\033[0m' % length)
  
  num = random.randint(1,length)
  print('\033[32;1m num is %d  green\033[0m' % num)
  for i in range(1, length+1):    # [1, 2, 3,...]
    for j in range(1, i+1):      # i->1:[1], i->2: [1, 2],...
      print('%s * %s= %s' % (j, i, i*j), end='\033[30;42;1m$$\033[0m')
    print()
  return  'lucky number is '+str(num)
sys.stdout.write('\033[30;41;1m %s \n\033[0m' % function())

