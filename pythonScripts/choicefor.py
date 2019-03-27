#!/usr/bin/env   python3
import  sys,random
from  string  import  digits,ascii_letters

nuber = random.randint(3,9)
sys.stdout.write("\033[30;42;1m nuber  is  %s \n\033[0m" % nuber)
sys.stdout.write("\033[30;43;1m __name__  is  %s \n\033[0m" % __name__)

#all_chars = string.digits + string.ascii_letters
all_chars = digits + ascii_letters

def  gen_pass(length = 4 ):
  result = [random.choice(all_chars)  for  i  in range(length)]
  print("result  is %s\t type is " % result,type(result))
  return  ''.join(result)  #将列表的字符拼接起来

if  __name__ == '__main__' :

  print("\033[31;1mDefault 4-bit password is red %s\033[0m" % gen_pass())
  print('The password random selection is ' + gen_pass(nuber))

