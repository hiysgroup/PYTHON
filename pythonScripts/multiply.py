#!/usr/bin/env   python3
import  random
import  getpass
import  sys

length = int(getpass.getpass('\033[30;43;1m yellow input digital length: \033[0m'))
num = random.randint(1,length)
def  multiply(length,num):
  print('\033[31;1m The integer length is %d  red\033[0m' % length)
  print('\033[32;1m num is %d  green\033[0m' % num)
  for i in range(1, length+1):    # [1, 2, 3,...]
    for j in range(1, i+1):      # i->1:[1], i->2: [1, 2],...
      print('%d * %d\033[33;1m=\033[0m %d' % (j, i, i*j), end='\033[30;42;1m$ \033[0m')
    sys.stdout.write('\033[31;43;1m \n\033[0m')
  fib = [0,1]
  for k  in  range(length - 2):
    fib.append(fib[-1] + fib [-2])
  sys.stdout.write('\033[30;42;1m green %s \n\033[0m' % fib)
  return  fib

outer = multiply(length,num)
with  open('fib.txt','w') as fobj:
  sys.stdout.write('\033[30;41;1m red write into fib.txt\n\033[0m')
  fobj.write(str(outer))

fobja = open('fib.txt','a')
try:
  fobja.seek(0,2)
  fobja.write('add try-finally\n')
  print('\033[32;1m try-finally add  green\033[0m')
finally:
  fobja.close()

with  open('fib.txt','r') as frobj:
  sys.stdout.write('\033[30;43;1m yellow fib.txt content is \033[0m')
  print(frobj.readlines())

