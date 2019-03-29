#!/usr/bin/env  python3
import  sys, os, getpass, string, keyword

sys.stdout.write('\033[33;40;1m__name__ yellow is %s\n\033[0m' % __name__)

first_chs = string.ascii_letters + '_'
all_chs = first_chs + string.digits

def   checkid(idt):
  if  len(idt) == 0:
    return 'Please input string!'
  elif idt[0] not in first_chs:
    return 'char %s invalid !' % idt[0]
  else:
    for (index,value)  in  enumerate(idt[1:]):
      if value not in all_chs:
        return 'The number %s char %s is invalid'% (index + 2,value)
    if keyword.iskeyword(idt):
      return 'string %s is keyword !' % idt
    return '%s is valid .' % idt


if __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s red\n\033[0m' % sys.argv)
  
  idt = input('input identifier: ')
  print(checkid(idt))

