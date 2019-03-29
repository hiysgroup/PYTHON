#!/usr/bin/env  python3
import  keyword, sys, os, getpass, shutil
"This  is a test module"
sys.stdout.write('\033[30;43;1m__name__ yellow is %s\n\033[0m' % __name__)

def  get_fname():
  while True:
    filename = input('Please input filename: ')
    if not  os.path.exists(filename):
      break
    print('\033[31;40;1m %s already exists\033[0m' % filename)
  return filename

def  get_contents():
  contents = []
  sys.stdout.write('\033[29;42;1m Please input content end with end\n\033[0m')
  while True:
    line = getpass.getpass('input content: ')
    if  line == 'end':
      break
    contents.append(line)
  return  contents

def  wfile(fname,contents):
  with open(fname,'w') as fobj:
    fobj.writelines(contents)

def  rmfile():
  boolrun = True
  filename = ''
  while boolrun:
    filename = input('input filename to be deleted: ')
    if not  os.path.exists(filename):
      print('\033[30;41;1m %s not exists\033[0m' % filename)
    else:
      print('\033[31;40;1m %s already exists\033[0m' % filename)
      confirm = input('remove filename  yes or no?: ')
      if confirm == 'yes':
        os.remove(filename)
        print('\033[31;40;1m %s is removed\033[0m' % filename)
        boolrun = False
  else:
    print('\033[32;40;1m file %s has been removed\033[0m' % filename)
    

if __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv[0] is %s red\n\033[0m' % sys.argv[0])
  sys.stdout.write('\033[32;48;1msys.argv is %s \n\033[0m' % sys.argv)
#  print(keyword.kwlist)
#  print(keyword.iskeyword('asxx'))
#  print(keyword.iskeyword('as'))
#  print('pass' in keyword.kwlist)
  fname = get_fname()
  contents = get_contents()
  contents = ['%s \n' % line for line  in contents]
  wfile(fname,contents)
  rmfile()
