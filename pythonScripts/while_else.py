#!/usr/bin/env  python3
import  random
import  getpass

num = random.randint(1,4)
print(type(num),end=' --num type\n')
print("num is\t" + str(num))

counter = 0
print("original counter is %s \t type is " % (counter),type(counter))

while  counter < 10:
  counter += 1
  if  counter %2 == 1:
     continue
  else:
    result = int(getpass.getpass('Guess the number: '))  
    if result > num:
      print('result is  %s Too Bigger' % (result))
      yn = input('Do you want to continue(y/n)? ')
      if yn == 'n':
        break
      print("continue running!")
    elif result < num:
      print('result is  %s Too Smaller' % (result))
      yn = input('Do you want to continue(y/n)? ')
      if yn == 'n':
        break
      print("continue running!")
    else:
      print("Guess Rightly!")
      break
  print("New counter is %s" % (counter))
else:
  print("End else num is %s,\tend counter is %s" % (num,counter))
