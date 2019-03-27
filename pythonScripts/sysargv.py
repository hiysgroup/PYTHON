#!/usr/bin/env   python3
import  random
import  getpass
import  sys

nuber = random.randint(1,100)
print("__name__  is  ",__name__)

def  copy(src_frb,dst_fwb):
#  src_frb = '/usr/bin/ls'
#  dst_fwb = '/tmp/newls'
  
  src_frb_obj = open(src_frb,'rb')
  dst_fwb_obj = open(dst_fwb,'wb')
  
  booleanrun = True
  while  booleanrun :
    frbdata = src_frb_obj.read(4096)
    if  frbdata ==  b'':
      booleanrun = False
    dst_fwb_obj.write(frbdata)
  else:
    src_frb_obj.close()
    dst_fwb_obj.close()
    print('Normal closure-------')

def  multiply(length = 4, num = 3):
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

def  withtry(outer):
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
  
if __name__ == '__main__':

  print(sys.argv)
  copy(sys.argv[1],sys.argv[2])
  
  length = int(getpass.getpass('\033[30;43;1m yellow input digital length: \033[0m'))
  
  num = random.randint(1,length)
  
  outer = multiply(length,num)
  withtry(outer)
  
