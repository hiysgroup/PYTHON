#!/usr/bin/env   python3
import  random
import  string
import  getpass
import  sys

nuber = random.randint(2,6)
sys.stdout.write("\033[30;42;1m nuber  is  %s \n\033[0m" % nuber)
sys.stdout.write("\033[30;43;1m __name__  is  %s \n\033[0m" % __name__)

all_chs = string.digits + string.ascii_letters
def  gen_pass(n = 4 ):
  result = ''
  for i  in range(n):
    choce = random.choice(all_chs)
    print("choce is %s" % choce)
    result += choce
    print("result is %s " % result)
  return  result

if  __name__ == '__main__' :

  print("\033[31;1mDefault 4-bit password is red %s\033[0m" % gen_pass())
  print('The password you chose is ' + gen_pass(nuber))

